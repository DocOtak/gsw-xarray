from functools import wraps
from itertools import chain

import gsw
import xarray as xr

from ._attributes import _func_attrs
from ._arguments import input_units
from ._names import _names
from ._check_funcs import _check_funcs
from ._function_utils import args_and_kwargs_to_kwargs

try:
    import pint_xarray
    import pint

except ImportError:
    pint_xarray = None


def add_attrs(rv, attrs, name):
    if isinstance(rv, xr.DataArray):
        rv.name = name
        rv.attrs = attrs


def quantify(rv, attrs, unit_registry=None):
    if unit_registry is None:
        return rv

    if isinstance(rv, xr.DataArray):
        rv = rv.pint.quantify(unit_registry=unit_registry)
    else:
        if attrs is not None:
            # Necessary to use the Q_ and not simply multiplication with ureg unit because of temperature
            # see https://pint.readthedocs.io/en/latest/nonmult.html
            rv = unit_registry.Quantity(rv, attrs["units"])
    return rv


def dequantify_reg(kw, arg):
    if isinstance(arg, xr.DataArray):
        if arg.pint.units is not None:
            try:
                input_unit = input_units[kw]
                _arg = arg.pint.to({arg.name: input_unit})
            except KeyError:
                _arg = arg
            # new_args.append(_arg.pint.dequantify())
            # registries.append(arg.pint.registry)
            _arg = _arg.pint.dequantify()
            _reg = arg.pint.registry
        else:
            _arg = arg
            _reg = None
    elif isinstance(arg, pint.Quantity):
        try:
            input_unit = input_units[kw]
            _arg = arg.to(input_unit)
        except KeyError:
            _arg = arg
        # new_args.append(_arg.magnitude)
        # registries.append(arg._REGISTRY)
        _arg = _arg.magnitude
        _reg = arg._REGISTRY
    else:
        # new_args.append(arg)
        _arg = arg
        _reg = None
    return _arg, _reg


def pint_compat(fname, kwargs):
    """
    fname : name of the function
    args_names : list of argument names of the function associated with *args*
    args, kwargs : list / dict of arguments and keyword arguments given to the function
        by the user
    """
    if pint_xarray is None:
        return args, kwargs, None

    new_kwargs = {}
    registries = []

    for kw, arg in kwargs.items():
        _arg, _reg = dequantify_reg(kw, arg)
        new_kwargs[kw] = _arg
        # We append registry only if kw has a unit, e.g. we skip it if kw is 'axis' or 'interp_method'
        if input_units[kw] is not None:
            registries.append(_reg)

    registries = set(registries)
    # If there is a None in registries, but len > 1 => error
    if (len(registries) > 1) and (None in registries):
        raise ValueError("Mixed usage of Quantity and non Quantity is forbidden.")

    try:
        registries.remove(None)
    except KeyError:
        pass

    if len(registries) > 1:
        raise ValueError(
            "Quantity arguments must all belong to the same unit registry."
        )
    elif len(registries) == 0:
        registries = None
    else:
        (registries,) = registries
    return new_kwargs, registries


def cf_attrs(fname, attrs, name, check_func):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            # We start by transforming all args to kwargs
            kwargs = args_and_kwargs_to_kwargs(func, args, kwargs)
            kwargs, unit_registry = pint_compat(fname, kwargs)
            rv = func(**kwargs)
            attrs_checked = check_func(attrs, kwargs)
            if isinstance(rv, tuple):
                rv_updated = []
                for (i, da) in enumerate(rv):
                    add_attrs(da, attrs_checked[i], name[i])
                    rv_updated.append(
                        quantify(da, attrs_checked[i], unit_registry=unit_registry)
                    )

                rv = tuple(rv_updated)

            else:
                add_attrs(rv, attrs_checked, name)
                rv = quantify(rv, attrs_checked, unit_registry=unit_registry)
            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator


def _init_funcs():
    _wrapped_funcs = {}
    for fname in _func_attrs.keys():
        _wrapped_funcs[fname] = cf_attrs(
            fname,
            _func_attrs[fname],
            _names[fname],
            _check_funcs.get(fname, lambda attrs, *args, **kwargs: attrs),
        )(getattr(gsw, fname))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()
