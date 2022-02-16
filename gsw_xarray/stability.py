from ._util import submodule_attr_compat, submodule_dir_compat, submodule_all_compat

__getattr__ = submodule_attr_compat("gsw.stability")
__dir__ = submodule_dir_compat("gsw.stability")
__all__ = submodule_all_compat("gsw.stability")
