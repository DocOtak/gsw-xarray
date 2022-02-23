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


_check_funcs = {"z_from_p": check_z_from_p}
