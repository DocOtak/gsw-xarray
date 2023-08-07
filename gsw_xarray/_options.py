"""
Started from xarray and cf_xarray options.py
"""

import copy

OPTIONS = {"non_cf_name": {}}


class set_options:
    """
    Set options for gsw_xarray in a controlled context.

    Parameters
    ----------
    non_cf_name : dict
        Provide the name in dataset of arguments that don't have a standard name
        e.g. {'entropy':'entropy_name_in_ds', 'SA_seaice':'salinity_of_sea_ice_name_in_ds'}

    You can use `set_options` either as a context manager (using `with`)
    or to set global options
    """

    def __init__(self, **kwargs):
        self.old = {}
        for k, v in kwargs.items():
            if k not in OPTIONS:
                raise ValueError(
                    f"argument name {k!r} is not in the set of valid options {set(OPTIONS)!r}"
                )
            self.old[k] = OPTIONS[k]
        self._apply_update(kwargs)

    def _apply_update(self, options_dict):
        options_dict = copy.deepcopy(options_dict)
        OPTIONS.update(options_dict)

    def __enter__(self):
        return

    def __exit__(self, type, value, traceback):
        self._apply_update(self.old)


def get_options():
    return copy.deepcopy(OPTIONS)


class set_non_cf_name(set_options):
    """
    Set `non_cf_name` options for gsw_xarray in a controlled context.

    Parameters
    ----------
    Provide the name in dataset of arguments that don't have a standard name
    e.g. entropy='entropy_name_in_ds', SA_seaice='salinity_of_sea_ice_name_in_ds'

    Using `set_non_cf_name` is equivalent to using `set_options`
    with argument 'set_non_cf_name', but is provided as a shorter method.

    You can use `set_non_cf_name` either as a context manager (using `with`)
    or to set global options
    """

    def __init__(self, **kwargs):
        self.old = {"non_cf_name": OPTIONS["non_cf_name"]}
        self._apply_update({"non_cf_name": kwargs})
