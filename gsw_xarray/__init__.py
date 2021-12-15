__version__ = "0.1.0"
from functools import wraps

import gsw
import xarray as xr


_func_standard_name_units = (
    ("CT_from_enthalpy", "sea_water_conservative_temperature", "degC"),
    ("CT_from_enthalpy_exact", "sea_water_conservative_temperature", "degC"),
    ("CT_from_entropy", "sea_water_conservative_temperature", "degC"),
    ("CT_from_pt", "sea_water_conservative_temperature", "degC"),
    ("CT_from_rho", "sea_water_conservative_temperature", "degC"),
    ("CT_from_t", "sea_water_conservative_temperature", "degC"),
    ("C_from_SP", "sea_water_electrical_conductivity", "mS cm-1"),
    ("SA_from_SP", "sea_water_absolute_salinity", "g kg-1"),
    ("SA_from_SP_Baltic", "sea_water_absolute_salinity", "g kg-1"),
    ("SA_from_Sstar", "sea_water_absolute_salinity", "g kg-1"),
    ("SA_from_rho", "sea_water_absolute_salinity", "g kg-1"),
    ("SP_from_C", "sea_water_practical_salinity", "1"),
    ("SP_from_SA", "sea_water_practical_salinity", "1"),
    ("SP_from_SA_Baltic", "sea_water_practical_salinity", "1"),
    ("SP_from_SK", "sea_water_practical_salinity", "1"),
    ("SP_from_SR", "sea_water_practical_salinity", "1"),
    ("SP_from_Sstar", "sea_water_practical_salinity", "1"),
    ("SP_salinometer", "sea_water_practical_salinity", "1"),
    ("SR_from_SP", "sea_water_reference_salinity", "g kg-1"),
    ("Sstar_from_SA", "sea_water_preformed_salinity", "g kg-1"),
    ("Sstar_from_SP", "sea_water_preformed_salinity", "g kg-1"),
    ("f", "coriolis_parameter", "s-1"),
    ("p_from_z", "sea_water_pressure", "dbar"),
    ("pt0_from_t", "sea_water_potential_temperature", "degC"),
    ("pt_from_CT", "sea_water_potential_temperature", "degC"),
    ("pt_from_entropy", "sea_water_potential_temperature", "degC"),
    # if p_ref is not 0 this next standard name is incorrect
    ("pt_from_t", "sea_water_potential_temperature", "degC"),
    ("rho", "sea_water_density", "kg m-3"),
    ("rho_t_exact", "sea_water_density", "kg m-3"),
    ("sigma0", "sea_water_sigma_t", "kg m-3"),  # only applies to pressure=0
    ("sound_speed", "speed_of_sound_in_sea_water", "m s-1"),
    ("sound_speed_t_exact", "speed_of_sound_in_sea_water", "m s-1"),
    ("t_from_CT", "sea_water_temperature", "degC"),
    # not sure how I feel about this next one
    ("z_from_p", "height_above_mean_sea_level", "m"),
)


def cf_attrs(standard_name, units, extra=None):
    def cf_attrs_decorator(func):
        @wraps(func)
        def cf_attrs_wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            if isinstance(rv, xr.DataArray):
                rv.attrs["standard_name"] = standard_name
                rv.attrs["units"] = units

            return rv

        return cf_attrs_wrapper

    return cf_attrs_decorator


def _init_funcs():
    _wrapped_funcs = {}
    for func, name, units in _func_standard_name_units:
        _wrapped_funcs[func] = cf_attrs(name, units)(getattr(gsw, func))
    return _wrapped_funcs


_wrapped_funcs = _init_funcs()


# See PEP 562
def __getattr__(name):
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
