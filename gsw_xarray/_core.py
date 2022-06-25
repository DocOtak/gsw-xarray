from functools import wraps, singledispatch

import gsw
import xarray as xr

from ._attributes import _func_attrs
from ._arguments import input_units
from ._names import _names
from ._check_funcs import _check_funcs
from ._function_utils import args_and_kwargs_to_kwargs
from ._units import safe_unit

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


@singledispatch
def convert_and_dequantify_reg(arg, kw):
    _arg = arg
    _reg = None
    return _arg, _reg


@convert_and_dequantify_reg.register
def _cd_xr(arg: xr.DataArray, kw):
    if arg.pint.units is not None:
        # pint-xarray raises ValueError if conversion does not work
        # so we split the choice of unit and conversion
        try:
            input_unit = input_units[kw]
        except KeyError:
            input_unit = arg.pint.units
        input_unit = safe_unit(input_unit, arg.pint.registry)
        _arg = arg.pint.to({arg.name: input_unit})
        _arg = _arg.pint.dequantify()
        _reg = arg.pint.registry
    else:
        _arg = arg
        _reg = None
    return _arg, _reg


if pint_xarray is not None:

    @convert_and_dequantify_reg.register
    def _cd_pint(arg: pint.Quantity, kw):
        try:
            input_unit = input_units[kw]
        except KeyError:
            input_unit = arg.unit
        input_unit = safe_unit(input_unit, arg._REGISTRY)
        _arg = arg.to(input_unit)
        _arg = _arg.magnitude
        _reg = arg._REGISTRY
        return _arg, _reg


def pint_compat(fname, kwargs):
    """
    Will convert to proper unit if Quantities are used, and dequantify arguments

    fname : name of the function
    kwargs : dict of keyword arguments given to the function
        by the user (all args must be previously transformed to kwargs)
    """
    if pint_xarray is None:
        return kwargs, None

    new_kwargs = {}
    registries = []

    for kw, arg in kwargs.items():
        # convert and dequantify
        # we can safely always call this due to the pint_xarray check above (and the base case of the single dispatch)
        _arg, _reg = convert_and_dequantify_reg(arg, kw)
        new_kwargs[kw] = _arg
        # We append registry only if kw has a unit, e.g. we skip it if kw is 'axis' or 'interp_method'
        if input_units[kw] is not None and _arg is not None:
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
            # We start by transforming all args to kwargs,
            # Except the default ones
            kwargs = args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults=False)
            kwargs, unit_registry = pint_compat(fname, kwargs)
            # We add the default arguments
            # It is necessary to not add defaults before pint compat
            # Otherwise, defaults are never Quantities
            kwargs = args_and_kwargs_to_kwargs(func, [], kwargs, add_defaults=True)
            # the upstream gsw does not treat equally args and kwargs so we get
            # back the original args
            o_args = list(kwargs.values())[: len(args)]
            o_kwargs = {i: kwargs[i] for i in list(kwargs)[len(args) :]}
            rv = func(*o_args, **o_kwargs)
            attrs_checked = check_func(attrs, kwargs)
            if isinstance(rv, tuple):
                rv_updated = []
                for (i, da) in enumerate(rv):
                    # Verify the unit
                    attrs_checked[i]["units"] = safe_unit(
                        attrs_checked[i]["units"], unit_registry
                    )
                    add_attrs(da, attrs_checked[i], name[i])
                    rv_updated.append(
                        quantify(da, attrs_checked[i], unit_registry=unit_registry)
                    )

                rv = tuple(rv_updated)

            else:
                # Verify the unit
                attrs_checked["units"] = safe_unit(
                    attrs_checked["units"], unit_registry
                )
                add_attrs(rv, attrs_checked, name)
                rv = quantify(rv, attrs_checked, unit_registry=unit_registry)
            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator


def _init_funcs():
    _wrapped_funcs = {}
    for fname, attrs in _func_attrs.items():
        _wrapped_funcs[fname] = cf_attrs(
            fname,
            attrs,
            _names[fname],
            _check_funcs[fname],
        )(getattr(gsw, fname))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()
