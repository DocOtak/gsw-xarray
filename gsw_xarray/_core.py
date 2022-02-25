from functools import wraps

import gsw
import xarray as xr

from ._attributes import _func_attrs
from ._names import _names
from ._check_funcs import _check_funcs


def add_attrs(rv, attrs, name):
    rv.name = name
    rv.attrs = attrs


def cf_attrs(attrs, name, check_func):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            attrs_checked = check_func(attrs, args, kwargs)
            if isinstance(rv, tuple):
                for (i, da) in enumerate(rv):
                    add_attrs(da, attrs_checked[i], name[i])
            elif isinstance(rv, xr.DataArray):
                add_attrs(rv, attrs_checked, name)
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
