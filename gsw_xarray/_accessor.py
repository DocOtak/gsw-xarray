"""
xarray Dataset accessor for gsw
"""

import xarray as xr

try:
    import cf_xarray
except ImportError:
    cf_xarray = None

from ._function_utils import args_and_kwargs_to_kwargs, parameters_as_set
from ._arguments import input_properties
from ._util import get_attribute
from ._core import _wrapped_funcs


def wrap_with_ds(ds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if cf_xarray is not None:
                # We transform all args to kwargs,
                # Except the default ones
                kwargs = args_and_kwargs_to_kwargs(
                    func, args, kwargs, add_defaults=False
                )
                # We add the missing arguments that we find in ds
                # 1) get the missing arguments
                parameters = parameters_as_set(func)
                missing_params = parameters - set(kwargs.keys())
                # 2) add them to kwargs
                kwargs.update(
                    {
                        i: ds.cf[input_properties[i]["standard_name"]]
                        for i in missing_params
                    }
                )
                # the upstream gsw does not treat equally args and kwargs so we get
                # back the original args
                o_args = list(kwargs.values())[: len(args)]
                o_kwargs = {i: kwargs[i] for i in list(kwargs)[len(args) :]}
                return func(*o_args, **o_kwargs)
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator


@xr.register_dataset_accessor("gsw")
class gswDatasetAccessor:
    """
    Dataset accessor for gsw
    """

    def __init__(self, ds):
        self._ds = ds
        self.__dict__.update(
            {
                name: wrap_with_ds(self._ds)(get_attribute(name))
                for name in _wrapped_funcs
            }
        )

    def __getitem__(self, name):
        return wrap_with_ds(self._ds)(get_attribute(name)).__call__()
