from gsw_xarray import __version__
import gsw_xarray as gsw
import xarray as xr

def _create_ds():
    import numpy as np
    ds = xr.Dataset()
    id = np.arange(3)
    ds['id'] = xr.DataArray(id, coords={'id':id})
    ds['CT'] = ds['id'] * 10
    ds['CT'].attrs = {'standard_name':'sea_water_conservative_temperature'}
    ds['SA'] = ds['id'] * 0.1 + 34
    ds['SA'].attrs = {'standard_name':'sea_water_absolute_salinity'}
    return ds

def test_version():
    assert __version__ == "0.1.0"

def test_func_standard():
    """Basic test"""
    ds = _create_ds()
    sigma0 = gsw.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'

def test_func_standard_module():
    """gsw can be used with modules, e.g. gsw.density, or e.g. 'import sigma0 from gsw.density'"""
    ds = _create_ds()
    # 
    sigma0 = gsw.density.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'
    #
    from gsw.density import sigma0
    sigma0 = sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'
    #
    from gsw import density
    sigma0 = density.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'
    #
    from gsw.density import * # Not good to do, but checks if functions are loaded
    sigma1 # should be loaded
    
