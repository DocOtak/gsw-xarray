from gsw_xarray import __version__
import gsw_xarray as gsw

def test_version():
    assert __version__ == "0.1.0"

def test_func_standard(ds):
    """Basic test"""
    sigma0 = gsw.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs['standard_name'] == 'sea_water_sigma_t'
    assert sigma0.name == 'sigma0'
    assert sigma0.attrs['units'] == "kg m^-3"
