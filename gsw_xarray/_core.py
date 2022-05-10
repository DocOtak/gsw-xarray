from functools import wraps
from itertools import chain

import gsw
import xarray as xr

from ._attributes import _func_attrs
from ._names import _names
from ._check_funcs import _check_funcs

try:
    import pint_xarray
    import pint

    ureg = pint.UnitRegistry()
    Q_ = ureg.Quantity
except ImportError:
    pint_xarray = None


def add_attrs(rv, attrs, name):
    if isinstance(rv, xr.DataArray):
        rv.name = name
        rv.attrs = attrs


def quantify(rv, attrs):
    if isinstance(rv, xr.DataArray):
        rv = rv.pint.quantify()
    else:
        if attrs is not None:
            rv = Q_(rv, attrs["units"])
    return rv


def pint_compat(args, kwargs):
    if pint_xarray is None:
        return args, kwargs, False

    using_pint = False
    new_args = []
    new_kwargs = {}
    for arg in args:
        if isinstance(arg, xr.DataArray):
            if arg.pint.units is not None:
                new_args.append(arg.pint.dequantify())
                using_pint = True
            else:
                new_args.append(arg)
        elif isinstance(arg, pint.Quantity):
            new_args.append(arg.magnitude)
            using_pint = True
        else:
            new_args.append(arg)

    for kw, arg in kwargs.items():
        if isinstance(arg, xr.DataArray):
            if arg.pint.units is not None:
                new_kwargs[kw] = arg.pint.dequantify()
                using_pint = True
            else:
                new_kwargs[kw] = arg
        elif isinstance(arg, pint.Quantity):
            new_kwargs[kw] = arg.magnitude
            using_pint = True
        else:
            new_kwargs[kw] = arg

    return new_args, new_kwargs, using_pint


def cf_attrs(attrs, name, check_func):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            args, kwargs, is_quantity = pint_compat(args, kwargs)
            rv = func(*args, **kwargs)
            attrs_checked = check_func(attrs, args, kwargs)
            if isinstance(rv, tuple):
                rv_updated = []
                for (i, da) in enumerate(rv):
                    add_attrs(da, attrs_checked[i], name[i])
                    if is_quantity:
                        rv_updated.append(quantify(da, attrs_checked[i]))
                    else:
                        rv_updated.append(da)

                rv = tuple(rv_updated)

            else:
                add_attrs(rv, attrs_checked, name)
                if is_quantity:
                    rv = quantify(rv, attrs_checked)
            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator


def _init_funcs():
    _wrapped_funcs = {}
    for func in _func_attrs.keys():
        _wrapped_funcs[func] = cf_attrs(
            _func_attrs[func],
            _names[func],
            _check_funcs.get(func, lambda attrs, *args, **kwargs: attrs),
        )(getattr(gsw, func))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()
