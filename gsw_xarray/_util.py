from importlib import import_module

import gsw

from ._core import _wrapped_funcs

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


def get_attribute(name):
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
