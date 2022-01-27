from ._util import submodule_attr_compat, submodule_dir_compat

__getattr__ = submodule_attr_compat("gsw.freezing")
__dir__ = submodule_dir_compat("gsw.freezing")