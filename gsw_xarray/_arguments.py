input_properties = {
    "C":{'units': "mS/cm"},
    "CT":{'units': "degC"},
    "Rt":{'units': "1"},
    "SA":{'units': "g/kg"},
    "SA_bulk":{'units': "g/kg"},
    "SA_seaice":{'units': "g/kg"},
    "SK":{'units': "1"},  # Initially part per thousand, but ppt is already used for picopint
    "SP":{'units': "1"},
    "SR":{'units': "g/kg"},
    "Sstar":{'units': "g/kg"},
    "axis":{'units': None},  # int, numpy axis
    "entropy":{'units': "J/(kg*K)"},
    "geo_strf":{'units': "m^2/s^2"},
    "geo_strf_dyn_height":{'units': "m^2/s^2"},
    "h":{'units': "J/kg"},
    "h_bulk":{'units': "J/kg"},
    "h_pot_bulk":{'units': "J/kg"},
    "interp_method":{'units': None},
    "lat":{'units': "degree_north"},
    "lon":{'units': "degree_east"},
    "max_dp":{'units': "dbar"},  # in geo_strf_dyn_height
    "p":{'units': "dbar"},
    "p_deep":{'units': "dbar"},
    "p_ref":{'units': "dbar"},
    "p_shallow":{'units': "dbar"},
    "pot_enthalpy_ice":{'units': "J/kg"},
    "pt":{'units': "degC"},
    "pt0":{'units': "degC"},
    "pt0_ice":{'units': "degC"},
    "rho":{'units': "kg/m^3"},
    "saturation_fraction":{'units': "1"},  # saturation_fraction must be between 0 and 1, and the default is 0, air free
    "sea_surface_geopotential":{'units': "m^2/s^2"},
    "t":{'units': "degC"},
    "t68":{'units': "degC"},
    "t_Ih":{'units': "degC"},
    "t_seaice":{'units': "degC"},
    "w_Ih":{'units': "1"},  # mass fraction of ice, w_Ih must be between 0 and 1.
    "w_seaice":{'units': "1"},  # mass fraction of sea ice, w_seaice must be between 0 and 1.
    "z":{'units': "m"},  # while z is positive in the atmosphere, it is NEGATIVE in the ocean.
}
