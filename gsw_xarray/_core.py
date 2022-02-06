from functools import wraps

import gsw
import xarray as xr

from ._attributes import _func_standard_name_units

def cf_attrs(attrs, extra=None):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            if isinstance(rv, xr.DataArray):
                rv.attrs = attrs

            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator

def _init_funcs():
    _wrapped_funcs = {}
    for func in _func_standard_name_units.keys():
        _wrapped_funcs[func] = cf_attrs(_func_standard_name_units[func])(getattr(gsw, func))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()
