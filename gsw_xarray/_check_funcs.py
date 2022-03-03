def check_pot_rho_t_exact(attrs, args, kwargs):
    """
    From cf convention:
    Sea water potential density is the density a parcel of sea water would have if moved adiabatically to a reference pressure, by default assumed to be sea level pressure. To specify the reference pressure to which the quantity applies, provide a scalar coordinate variable with standard name reference_pressure. The density of a substance is its mass per unit volume. For sea water potential density, if 1000 kg m-3 is subtracted, the standard name sea_water_sigma_theta should be chosen instead.
    """
    return attrs


def check_z_from_p(attrs, args, kwargs):
    """
    If the 2 optional arguments are not 0, removes the standard name.

    Reminder of the function call:
    gsw.z_from_p(p, lat, geo_strf_dyn_height=0, sea_surface_geopotential=0)

    Parameters
    ----------
    args and kwargs : list and dict
        the arguments passed to gsw.z_from_p
    attrs : dict
        the attributes associated with the function z_from_p
    (e.g. standard_name, units, etc)
    """
    # Getting the values of optional parameters
    # If the values are in kwargs, all good
    # Otherwise, we get them from args
    try:
        geo_strf_dyn_height = kwargs["geo_strf_dyn_height"]
    except KeyError:
        try:
            geo_strf_dyn_height = args[2]
        except IndexError:
            geo_strf_dyn_height = 0  # Could use inspect.signature to get default value

    try:
        sea_surface_geopotential = kwargs["sea_surface_geopotential"]
    except KeyError:
        try:
            sea_surface_geopotential = args[3]
        except IndexError:
            sea_surface_geopotential = (
                0  # Could use inspect.signature to get default value
            )

    if geo_strf_dyn_height != 0 or sea_surface_geopotential != 0:
        attrs = attrs.copy()
        # necessary to use a copy, or it will pop the item from the original dict
        attrs.pop("standard_name")
    return attrs


_check_funcs = {
    "pot_rho_t_exact": check_pot_rho_t_exact,
    "z_from_p": check_z_from_p,
}

# TODO
# sigma1, sigma2, sigma3, sigma4
