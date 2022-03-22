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
except ImportError:
    pint_xarray = None


def add_attrs(rv, attrs, name):
    rv.name = name
    rv.attrs = attrs


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
                        da = rv.pint.quantify()
                        rv_updated.append(da)
                    else:
                        rv_updated.append(da)

                rv = tuple(rv_updated)

            elif isinstance(rv, xr.DataArray):
                add_attrs(rv, attrs_checked, name)
                if is_quantity:
                    rv = rv.pint.quantify()
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
