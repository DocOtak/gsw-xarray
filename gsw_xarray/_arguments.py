input_units = {
    "C": "mS/cm",
    "CT": "degC",
    "Rt": "1",
    "SA": "g/kg",
    "SA_bulk": "g/kg",
    "SA_seaice": "g/kg",
    "SK": "1",  # Initially part per thousand, but ppt is already used for picopint
    "SP": "1",
    "SR": "g/kg",
    "Sstar": "g/kg",
    "axis": None,  # int, numpy axis
    "entropy": "J/(kg*K)",
    "geo_strf": "m^2/s^2",
    "geo_strf_dyn_height": "m^2/s^2",
    "h": "J/kg",
    "h_bulk": "J/kg",
    "h_pot_bulk": "J/kg",
    "interp_method": None,
    "lat": "degree_north",
    "lon": "degree_east",
    "max_dp": "dbar",  # in geo_strf_dyn_height
    "p": "dbar",
    "p_deep": "dbar",
    "p_ref": "dbar",
    "p_shallow": "dbar",
    "pot_enthalpy_ice": "J/kg",
    "pt": "degC",
    "pt0": "degC",
    "pt0_ice": "degC",
    "rho": "kg/m^3",
    "saturation_fraction": "1",  # saturation_fraction must be between 0 and 1, and the default is 0, air free
    "sea_surface_geopotential": "m^2/s^2",
    "t": "degC",
    "t68": "degC",
    "t_Ih": "degC",
    "t_seaice": "degC",
    "w_Ih": "1",  # mass fraction of ice, w_Ih must be between 0 and 1.
    "w_seaice": "1",  # mass fraction of sea ice, w_seaice must be between 0 and 1.
    "z": "m",  # while z is positive in the atmosphere, it is NEGATIVE in the ocean.
}
