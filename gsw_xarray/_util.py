from importlib import import_module

from ._core import _wrapped_funcs


def submodule_attr_compat(submodule_name):
    submodule = import_module(submodule_name)

    def getattr_(name):
        # this will raise name error if not in the wrapped implimentation, this is desireable
        default = getattr(submodule, name)
        return _wrapped_funcs.get(name, default)

    return getattr_


def submodule_dir_compat(submodule_name):
    submodule = import_module(submodule_name)

    def dir_(name):
        return dir(submodule)
