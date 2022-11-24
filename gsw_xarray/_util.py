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


def submodule_attr_compat(submodule_name):
    submodule = import_module(submodule_name)

    def getattr_(name):
        # this will raise name error if not in the wrapped implimentation, this is desireable
        default = getattr(submodule, name)
        return _wrapped_funcs.get(name, default)

    return getattr_


def submodule_dir_compat(submodule_name):
    submodule = import_module(submodule_name)

    def dir_():
        return dir(submodule)

    return dir_


def submodule_all_compat(submodule_name):
    submodule = import_module(submodule_name)
    try:
        return submodule.__all__
    except AttributeError:
        all = dir(submodule)
        # as per python docs, an import * should return everything not starting with "_"
        return list(filter(lambda s: not s.startswith("_"), all))


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
