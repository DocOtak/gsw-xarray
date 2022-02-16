from functools import wraps

import gsw
import xarray as xr

from ._cf_names import _func_standard_name_units


def cf_attrs(standard_name, units, extra=None):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            if isinstance(rv, xr.DataArray):
                rv.attrs["standard_name"] = standard_name
                rv.attrs["units"] = units

            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator


def _init_funcs():
    _wrapped_funcs = {}
    for func, name, units in _func_standard_name_units:
        _wrapped_funcs[func] = cf_attrs(name, units)(getattr(gsw, func))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()
