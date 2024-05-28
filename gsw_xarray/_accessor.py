"""
xarray Dataset accessor for gsw
"""

from functools import wraps

import gsw
import xarray as xr

try:
    import cf_xarray
except ImportError:
    cf_xarray = None


from ._core import _wrapped_funcs
from ._function_utils import (
    args_and_kwargs_to_kwargs,
    get_parameters_standard_name,
    parameters_as_set,
)
from ._options import get_options
from ._util import get_attribute


def safe_get_cf(ds, n):
    if n in ds:
        return n
    return ds.cf[n]


def parameter_from_standard_name(std_nme, names_missing_params):
    for i in names_missing_params:
        if names_missing_params[i] == std_nme:
            return i
        elif std_nme in names_missing_params[i] and isinstance(
            names_missing_params[i], list
        ):
            return i
    return None


def wrap_with_ds(ds):
    def decorator(func):
        @wraps(func)
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
                #
                # The order of priority is:
                # A. user set option cf_name_preference
                # B. the reference standard names
                # C. user set option non_cf_name
                #
                OPTIONS = get_options()
                # We will do multiple loops for clarity
                #
                # A. user set option cf_name_preference
                # We start with names in ds taken from cf_name_preference
                standard_names_missing_params = get_parameters_standard_name(
                    func.__name__, missing_params
                )
                standard_names_missing_params_flatten = [
                    item
                    for sublist in standard_names_missing_params.values()
                    for item in sublist
                ]
                for std_nme in set(standard_names_missing_params_flatten).intersection(
                    OPTIONS["cf_name_preference"].keys()
                ):
                    # Here we get the standard names that are both in user option and parameter of the function
                    # We  need to get the original parameter name
                    p = parameter_from_standard_name(
                        std_nme, standard_names_missing_params
                    )
                    kwargs.update({p: ds[OPTIONS["cf_name_preference"][std_nme]]})
                    missing_params -= {p}

                # B. the reference standard names
                # Actualize argument standard names
                standard_names_missing_params = get_parameters_standard_name(
                    func.__name__, missing_params
                )
                standard_names_missing_params_flatten = [
                    item
                    for sublist in standard_names_missing_params.values()
                    for item in sublist
                ]
                ds_cf_standard_names = ds.cf.standard_names
                ds_cf_standard_names_keys = ds_cf_standard_names.keys()
                for p in standard_names_missing_params:
                    out = []
                    for std_nme in standard_names_missing_params[p]:
                        if std_nme in ds_cf_standard_names_keys:
                            # out.append(ds.cf[std_nme])
                            cf_xarray_detected_vars = ds_cf_standard_names[std_nme]
                            if len(cf_xarray_detected_vars) > 1:
                                raise (
                                    KeyError(
                                        f"Argument '{p}' of function '{func.__name__}'"
                                        + f" with standard name {standard_names_missing_params[p]}"
                                        + " has been found multiple times in the dataset: "
                                        + f"{cf_xarray_detected_vars}"
                                    )
                                )
                            out.append(ds[cf_xarray_detected_vars[0]])
                    if out == []:
                        raise (
                            TypeError(
                                f"Argument '{p}' of function '{func.__name__}' "
                                + f"with standard name {standard_names_missing_params[p]}"
                                + " is not present in the dataset"
                            )
                        )
                    elif len(out) > 1:
                        raise (
                            TypeError(
                                f"Argument '{p}' of function '{func.__name__}'"
                                + f" with standard name {standard_names_missing_params[p]}"
                                + " has been found multiple times in the dataset:"
                                + f"{[i.name for i in out]}"
                            )
                        )
                    kwargs.update({p: out[0]})
                    missing_params -= {p}

                # C. user set option non_cf_name
                for p in missing_params:
                    if p not in OPTIONS["non_cf_name"]:
                        raise (
                            TypeError(
                                f"Argument '{i}' of function '{func.__name__}' does"
                                + " not have a cf standard name: you need to provide"
                                + " this argument"
                            )
                        )
                    kwargs.update({p: ds[OPTIONS["non_cf_name"][p]]})

                # the upstream gsw does not treat equally args and kwargs so we get
                # back the original args
                o_args = list(kwargs.values())[: len(args)]
                o_kwargs = {i: kwargs[i] for i in list(kwargs)[len(args) :]}
                return func(*o_args, **o_kwargs)
            else:
                return func(*args, **kwargs)

        # Add doc for standard names
        parameters = parameters_as_set(func)
        standard_names = get_parameters_standard_name(func.__name__, parameters)
        wrapper.__doc__ += (
            f"\ngsw_xarray accessor version of gsw.{func.__name__}, the following arguments have standard names:\n"
            + "\n".join([f"{i}: {v}" for i, v in standard_names.items()])
        )
        return wrapper

    return decorator


def _test_if_wrapped(name):
    if name in _wrapped_funcs:
        return
    try:
        getattr(gsw, name)
        raise AttributeError(
            f"{name} has not been mapped by gsw_xarray in the xarray accessor. "
            + "You can access it with `gsw.{name}`"
        )
    except AttributeError:
        raise AttributeError(f"{name} does not exist in the upstream gsw library")


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
            for i in name:
                _test_if_wrapped(i)
            return xr.merge(
                [wrap_with_ds(self._ds)(get_attribute(i)).__call__() for i in name],
                combine_attrs="drop",
            )
        else:
            _test_if_wrapped(name)
            return wrap_with_ds(self._ds)(get_attribute(name)).__call__()
