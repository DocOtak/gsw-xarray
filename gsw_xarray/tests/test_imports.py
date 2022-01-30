import pytest
from ._data import create_ds

"""
Here all import machinery is tested (dir, getattr, ...),
for functions and modules.

The import gsw_xarray is kept in every function to not interfere
between them with a global import.
"""

def test_func_standard_dir():
    """Test with dir"""
    ds = create_ds()
    import gsw_xarray
    assert 'sigma0' in dir(gsw_xarray)

def test_func_standard_getattr():
    """Test with dir"""
    ds = create_ds()
    import gsw_xarray
    assert 'sigma0' in dir(gsw_xarray)
    with pytest.raises(AttributeError):
        getattr(gsw_xarray, 'no_function')
    
def test_func_standard_module():
    """gsw can be used with modules"""
    import gsw_xarray as gsw
    ds = create_ds()
    sigma0 = gsw.density.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'

def test_func_standard_module_import_from_module():
    """gsw can be used with modules"""
    ds = create_ds()
    from gsw_xarray.density import sigma0
    sigma0 = sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'

def test_func_standard_module_import_module():
    """gsw can be used with modules"""
    ds = create_ds()
    from gsw_xarray import density
    sigma0 = density.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'

def test_func_standard_module_dir():
    """gsw can be used with modules"""
    ds = create_ds()
    import gsw_xarray.density
    assert 'sigma0' in dir(gsw_xarray.density)
    import gsw_xarray.ice
    assert 'sigma0' not in dir(gsw_xarray.ice)

def test_func_standard_module_getattr():
    """gsw can be used with modules"""
    ds = create_ds()
    import gsw_xarray.density
    getattr(gsw_xarray.density, 'sigma0')
    import gsw_xarray.ice
    with pytest.raises(AttributeError):
        getattr(gsw_xarray.ice, 'sigma0')
