input_properties = {
    "C": {
        "units": "mS/cm",
        "standard_name": "sea_water_electrical_conductivity",
    },
    "CT": {
        "units": "degC",
        "standard_name": "sea_water_conservative_temperature",
    },
    "Rt": {"units": "1"},
    "SA": {
        "units": "g/kg",
        "standard_name": "sea_water_absolute_salinity",
    },
    "SA_bulk": {"units": "g/kg"},
    "SA_seaice": {"units": "g/kg"},
    "SK": {
        "units": "1"
    },  # Initially part per thousand, but ppt is already used for picopint
    "SP": {
        "units": "1",
        "standard_name": ["sea_water_practical_salinity", "sea_water_salinity"],
        # This 2nd standard name is the old one, still used e.g. in ARGO
    },
    "SR": {"units": "g/kg"},
    "Sstar": {"units": "g/kg"},
    "axis": {"units": None},  # int, numpy axis
    "entropy": {"units": "J/(kg*K)"},
    "geo_strf": {"units": "m^2/s^2"},
    "geo_strf_dyn_height": {"units": "m^2/s^2"},
    "h": {"units": "J/kg"},
    "h_bulk": {"units": "J/kg"},
    "h_pot_bulk": {"units": "J/kg"},
    "interp_method": {"units": None},
    "lat": {
        "units": "degree_north",
        "standard_name": "latitude",
    },
    "lon": {
        "units": "degree_east",
        "standard_name": "longitude",
    },
    "max_dp": {"units": "dbar"},  # in geo_strf_dyn_height
    "p": {
        "units": "dbar",
    },
    "p_deep": {"units": "dbar"},
    "p_ref": {"units": "dbar"},
    "p_shallow": {"units": "dbar"},
    "pot_enthalpy_ice": {"units": "J/kg"},
    "pt": {
        "units": "degC",
        "standard_name": "sea_water_potential_temperature",
    },
    "pt0": {"units": "degC"},
    "pt0_ice": {"units": "degC"},
    "rho": {
        "units": "kg/m^3",
        "standard_name": "sea_water_density",
    },
    "saturation_fraction": {
        "units": "1"
    },  # saturation_fraction must be between 0 and 1, and the default is 0, air free
    "sea_surface_geopotential": {"units": "m^2/s^2"},
    "t": {
        "units": "degC",
    },
    "t68": {"units": "degC"},
    "t_Ih": {"units": "degC"},
    "t_seaice": {"units": "degC"},
    "w_Ih": {"units": "1"},  # mass fraction of ice, w_Ih must be between 0 and 1.
    "w_seaice": {
        "units": "1"
    },  # mass fraction of sea ice, w_seaice must be between 0 and 1.
    "z": {
        "units": "m",
        "standard_name": "height_above_mean_sea_level",
    },  # while z is positive in the atmosphere, it is NEGATIVE in the ocean.
}
