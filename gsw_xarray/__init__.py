__version__ = "0.5.0"

import gsw

import gsw_xarray._accessor  # noqa: F401

from ._core import _wrapped_funcs
from ._options import (  # noqa: F401
    get_options,
    set_cf_name_preference,
    set_non_cf_name,
    set_options,
)
from ._util import _compat, get_attribute
from ._util_module import submodule_all_compat

gsw_xarray_specific_functions = [
    "set_options",
    "get_options",
    "set_non_cf_name",
    "set_cf_name_preference",
]


__all__ = submodule_all_compat("gsw") + list(_compat)


# See PEP 562
def __getattr__(name):
    return get_attribute(name)


def __dir__():
    return list(
        sorted(set([*_wrapped_funcs.keys(), *dir(gsw), *gsw_xarray_specific_functions]))
    )
