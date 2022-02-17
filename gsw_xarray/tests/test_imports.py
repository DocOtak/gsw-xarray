from types import ModuleType
import numpy as np

import pytest

"""
Here all import machinery is tested (dir, getattr, ...),
for functions and modules.

The import gsw_xarray is kept in every function to not interfere
between them with a global import.
"""

import gsw_xarray
import gsw


def get_module_names(module):
    mod_names = dir(module)

    # filter out all the "private" names
    public_names = list(filter(lambda name: not name.startswith("_"), mod_names))

    # filter out modules
    return list(
        filter(
            lambda name: not isinstance(getattr(module, name), ModuleType), public_names
        )
    )


gsw_base = get_module_names(gsw)
wrapped_funcs = gsw_xarray._core._wrapped_funcs

submodules = [
    "conversions",
    "density",
    "energy",
    "freezing",
    "geostrophy",
    "ice",
    "stability",
]


@pytest.mark.parametrize("upstream_func", gsw_base)
def test_wrapped_interface(upstream_func):
    """Tests the complete gsw function namespace against ours"""
    assert hasattr(gsw_xarray, upstream_func)


@pytest.mark.parametrize("upstream_func", gsw_base)
def test_wrapped_return(upstream_func):
    if upstream_func in wrapped_funcs:
        assert getattr(gsw_xarray, upstream_func) is wrapped_funcs[upstream_func]
    else:
        assert getattr(gsw_xarray, upstream_func) is getattr(gsw, upstream_func)


@pytest.mark.parametrize("submodule", submodules)
def test_wrapped_interface_submodules(submodule):
    upstream_submodule = getattr(gsw, submodule)
    wrapped_submodule = getattr(gsw_xarray, submodule)

    upstream_funcs = get_module_names(upstream_submodule)
    for name in upstream_funcs:
        if name in wrapped_funcs:
            assert getattr(wrapped_submodule, name) is wrapped_funcs[name]
        else:
            assert getattr(wrapped_submodule, name) is getattr(upstream_submodule, name)


@pytest.mark.parametrize("upstream_func", gsw_base)
def test_import_interface_base(upstream_func):
    """This tests the interface in the form of:
    > from gsw_xarray import func
    where func is any function on the upstream gsw

    It does this by creating an empty "locals" dict and calling an exec on the way the code
    would be written, it then checks the idenity of that returned result
    """
    result = {}
    # the empty dict is for the "globals" that we don't care about (exec would populate it with builtins)
    exec(f"from gsw_xarray import {upstream_func}", {}, result)
    func = result[upstream_func]
    if upstream_func in wrapped_funcs:
        assert func is wrapped_funcs[upstream_func]
    else:
        assert func is getattr(gsw, upstream_func)


@pytest.mark.parametrize("upstream_func", gsw_base)
@pytest.mark.parametrize("submodule", submodules)
def test_import_interface_submodule(submodule, upstream_func):
    """This tests the interface in the form of:
    > from gsw_xarray.submod import func
    where submod is one of the submodule groupings in the upstream

    """
    result = {}
    upstream_interface = get_module_names(getattr(gsw, submodule))

    expected_func = getattr(gsw, upstream_func)

    if upstream_func not in upstream_interface:
        with pytest.raises(ImportError):
            exec(f"from gsw_xarray.{submodule} import {upstream_func}", {}, result)
    else:
        exec(f"from gsw_xarray.{submodule} import {upstream_func}", {}, result)

        func = result[upstream_func]

        if isinstance(func, np.ufunc):
            pytest.xfail(f"{func} of submodule {submodule} is a directly exposed ufunc")

        if upstream_func in wrapped_funcs:
            assert func is wrapped_funcs[upstream_func]
        else:
            assert func is expected_func


@pytest.mark.parametrize("upstream_func", gsw_base)
@pytest.mark.parametrize("submodule", submodules)
def test_attr_method(submodule, upstream_func):
    """tests the identities of funcs in the form of gsw_xarray.submodule.func"""
    upstream_interface = get_module_names(getattr(gsw, submodule))

    expected_func = getattr(gsw, upstream_func)

    if upstream_func not in upstream_interface:
        with pytest.raises(AttributeError):
            eval(f"gsw_xarray.{submodule}.{upstream_func}")
    else:
        func = eval(f"gsw_xarray.{submodule}.{upstream_func}")

        if isinstance(func, np.ufunc):
            pytest.xfail(f"{func} of submodule {submodule} is a directly exposed ufunc")

        if upstream_func in wrapped_funcs:
            assert func is wrapped_funcs[upstream_func]
        else:
            assert func is expected_func


def test_wildcard_top_level():
    upstream_interface = {}
    exec("from gsw import *", {}, upstream_interface)

    wrapped_interface = {}
    exec("from gsw_xarray import *", {}, wrapped_interface)

    assert wrapped_interface.keys() == upstream_interface.keys()


@pytest.mark.parametrize("submodule", submodules)
def test_wildcard_submodule(submodule):
    """tests the identities of funcs in the form of gsw_xarray.submodule.func"""
    upstream_interface = {}
    exec(f"from gsw.{submodule} import *", {}, upstream_interface)

    wrapped_interface = {}
    exec(f"from gsw_xarray.{submodule} import *", {}, wrapped_interface)

    assert wrapped_interface.keys() == upstream_interface.keys()
