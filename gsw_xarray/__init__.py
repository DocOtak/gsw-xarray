__version__ = "0.3.0"

from importlib import import_module

import gsw
from ._core import _wrapped_funcs
from ._util import submodule_all_compat, get_attribute, _compat
import gsw_xarray._accessor
from ._options import set_options, get_options, set_non_cf_name, set_cf_name_preference

gsw_xarray_specific_functions = [
    "set_options",
    "get_options",
    "set_non_cf_name",
    "set_cf_name_preference",
]

_compat_modules = {name: import_module(f".{name}", "gsw_xarray") for name in _compat}

__all__ = submodule_all_compat("gsw") + list(_compat)

# See PEP 562
def __getattr__(name):
    return get_attribute(name)


def __dir__():
    return list(
        sorted(set([*_wrapped_funcs.keys(), *dir(gsw), *gsw_xarray_specific_functions]))
    )
