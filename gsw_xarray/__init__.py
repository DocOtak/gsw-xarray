__version__ = "0.2.1"

from importlib import import_module

import gsw
from ._core import _wrapped_funcs
from ._util import submodule_all_compat


_compat = {
    "conversions",
    "density",
    "energy",
    "freezing",
    "geostrophy",
    "ice",
    "stability",
}
_compat_modules = {name: import_module(f".{name}", "gsw_xarray") for name in _compat}

__all__ = submodule_all_compat("gsw") + list(_compat)

# See PEP 562
def __getattr__(name):
    if name in _compat:
        return getattr(_compat_modules[name], name)
    try:
        return _wrapped_funcs[name]
    except KeyError:
        try:
            return getattr(gsw, name)
        except AttributeError as error:
            raise AttributeError(
                f"module {__name__} has no attribute {name}"
            ) from error


def __dir__():
    return list(sorted(set([*_wrapped_funcs.keys(), *dir(gsw)])))
