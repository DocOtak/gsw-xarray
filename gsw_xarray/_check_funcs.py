def _rm_std_nme(d):
    """
    Return a dict which does not contain the standard name
    """
    d = d.copy()
    # necessary to use a copy, or it will pop the item from the original dict
    try:
        d.pop("standard_name")
    except KeyError:
        pass
    return d


def check_pot_rho_t_exact(attrs, args, kwargs):
    """
    If the reference pressure is not 0, remove standard name.

    Reminder of the function call:
    gsw.pot_rho_t_exact(SA, t, p, p_ref)

    TODO: could provide a scalar coordinate variable with standard name reference_pressure
    (see issue 32, https://github.com/DocOtak/gsw-xarray/issues/32)
    """
    # get value of p_ref
    try:
        p_ref = kwargs["p_ref"]
    except KeyError:
        p_ref = args[3]

    if p_ref == 0:
        return attrs
    else:
        return _rm_std_nme(attrs)


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
        return _rm_std_nme(attrs)
    else:
        return attrs


_check_funcs = {
    "pot_rho_t_exact": check_pot_rho_t_exact,
    "z_from_p": check_z_from_p,
}

# TODO
# sigma1, sigma2, sigma3, sigma4
