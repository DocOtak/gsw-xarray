from functools import wraps
from itertools import chain

import gsw
import xarray as xr

from ._attributes import _func_attrs
from ._arguments import _arg_attrs
from ._names import _names
from ._check_funcs import _check_funcs
from ._function_utils import get_args_names

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


def pint_compat(fname, args_names, args, kwargs):
    """
    fname : name of the function
    """
    if pint_xarray is None:
        return args, kwargs, None

    using_pint = False
    new_args = []
    new_kwargs = {}
    registries = []
    for i, arg in enumerate(args):
        if isinstance(arg, xr.DataArray):
            if arg.pint.units is not None:
                try:
                    input_unit = _arg_attrs[fname][args_names[i]]["units"]
                    _arg = arg.pint.to({arg.name:input_unit})
                except KeyError:
                    _arg = arg
                new_args.append(_arg.pint.dequantify())
                registries.append(arg.pint.registry)
            else:
                new_args.append(arg)
        elif isinstance(arg, pint.Quantity):
            try:
                input_unit = _arg_attrs[fname][args_names[i]]["units"]
                _arg = arg.to(input_unit)
            except KeyError:
                _arg = arg
            new_args.append(_arg.magnitude)
            registries.append(arg._REGISTRY)
        else:
            new_args.append(arg)

    for kw, arg in kwargs.items():
        if isinstance(arg, xr.DataArray):
            if arg.pint.units is not None:
                try:
                    input_unit = _arg_attrs[fname][kw]["units"]
                    _arg = arg.pint.to({arg.name:input_unit})
                except KeyError:
                    _arg = arg
                new_kwargs[kw] = _arg.pint.dequantify()
                registries.append(arg.pint.registry)
            else:
                new_kwargs[kw] = arg
        elif isinstance(arg, pint.Quantity):
            try:
                input_unit = _arg_attrs[fname][kw]["units"]
                _arg = arg.to(input_unit)
            except KeyError:
                _arg = arg
            new_kwargs[kw] = _arg.magnitude
            registries.append(arg._REGISTRY)
        else:
            new_kwargs[kw] = arg

    registries = set(registries)
    if len(registries) > 1:
        raise ValueError("Quantity arguments must all belong to the same unit registry")
    elif len(registries) == 0:
        registries = None
    else:
        (registries,) = registries
    return new_args, new_kwargs, registries


def cf_attrs(fname, attrs, name, check_func):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            args_names = get_args_names(func, args)
            args, kwargs, unit_registry = pint_compat(fname, args_names, args, kwargs)
            rv = func(*args, **kwargs)
            attrs_checked = check_func(attrs, args, kwargs)
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
