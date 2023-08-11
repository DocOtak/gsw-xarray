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
from ._options import get_options


def wrap_with_ds(ds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if cf_xarray is not None:
                # We transform all args to kwargs,
                # Except the default ones
                kwargs = args_and_kwargs_to_kwargs(
                    func, args, kwargs, add_defaults=False
                )
                # If arguments are string => replace with value from ds
                for i in kwargs:
                    if isinstance(kwargs[i], str):
                        kwargs[i] = ds[kwargs[i]]
                # We add the missing arguments that we find in ds
                # 1) get the missing arguments
                parameters = parameters_as_set(func)
                missing_params = parameters - set(kwargs.keys())
                # 2) add them to kwargs
                if "t" in missing_params:
                    if "ice" in func.__name__:
                        kwargs.update({"t": ds.cf["sea_ice_temperature"]})
                    else:
                        kwargs.update({"t": ds.cf["sea_water_temperature"]})
                    missing_params = missing_params - set("t")
                if "p" in missing_params:
                    if "ice" in func.__name__:
                        raise (
                            TypeError(
                                f"Argument 'p' for sea ice of function '{func.__name__}' does not have a cf standard name: you need to provide this argument"
                            )
                        )
                    else:
                        kwargs.update({"p": ds.cf["sea_water_pressure"]})
                    missing_params = missing_params - set("p")
                # We need to check that all missing arguments have a standard_name
                OPTIONS = get_options()
                for i in missing_params:
                    std_nme_raw = input_properties[i].get("standard_name")
                    std_nme = None
                    # In some cases, std_nme can be a list if multiple standard names exist
                    if isinstance(std_nme_raw, list):
                        ds_cf_standard_names_keys = ds.cf.standard_names.keys()
                        for name in std_nme_raw:
                            # We check and stop at the 1st occurence
                            if name in ds_cf_standard_names_keys:
                                std_nme = name
                                break
                    else:
                        std_nme = std_nme_raw

                    if std_nme is None:
                        # Check if the user provided options to retrieve the argument
                        std_nme = OPTIONS["non_cf_name"].get(i)
                    if std_nme is None:
                        raise (
                            TypeError(
                                f"Argument '{i}' of function '{func.__name__}' does not have a cf standard name: you need to provide this argument"
                            )
                        )
                    else:
                        kwargs.update({i: ds.cf[std_nme]})
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
        if isinstance(name, list):
            return xr.merge(
                [wrap_with_ds(self._ds)(get_attribute(i)).__call__() for i in name],
                combine_attrs="drop",
            )
        else:
            return wrap_with_ds(self._ds)(get_attribute(name)).__call__()
