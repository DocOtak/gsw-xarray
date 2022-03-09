_func_attrs = {
    "CT_first_derivatives": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "1",
        },
    ),
    "CT_first_derivatives_wrt_t_exact": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "1",
        },
        {
            "units": "K/Pa",
        },
    ),
    "CT_freezing": {
        "units": "degC",
        "reference_scale": "ITS-90",
        "standard_name": "freezing_temperature_of_sea_water",  # Not sure
    },
    "CT_freezing_first_derivatives": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "CT_freezing_first_derivatives_poly": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "CT_freezing_poly": {
        "units": "degC",
        "reference_scale": "ITS-90",
        "standard_name": "freezing_temperature_of_sea_water",  # Not sure
    },
    "CT_from_enthalpy": {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_from_enthalpy_exact": {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_from_entropy": {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_from_pt": {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_from_rho": (
        {
            "standard_name": "sea_water_conservative_temperature",
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "standard_name": "sea_water_conservative_temperature",
            "units": "degC",
            "reference_scale": "ITS-90",
        },
    ),
    "CT_from_t": {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_maxdensity": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "CT_second_derivatives": (
        {
            "units": "K/((g/kg)^2)",
        },
        {
            "units": "1/(g/kg)",
        },
        {
            "units": "1/K",
        },
    ),
    "C_from_SP": {
        "standard_name": "sea_water_electrical_conductivity",
        "units": "mS/cm",
    },
    "Fdelta": {
        "units": "1",
    },
    "Helmholtz_energy_ice": {
        "units": "J/kg",
    },
    "Hill_ratio_at_SP2": {
        "units": "1",
    },
    "IPV_vs_fNsquared_ratio": (
        {
            "units": "1",
        },
        {
            "standard_name": "sea_water_pressure",  # Not sure (is it tot pressure or only presure due to sea water?
            "units": "dbar",
        },
    ),
    "Nsquared": (
        {
            "standard_name": "square_of_brunt_vaisala_frequency_in_sea_water",
            "units": "rad^2 s^-2",  # Seems to be an error in the python doc, where it is 1/s
        },
        {
            "standard_name": "sea_water_pressure",  # Not sure (is it tot pressure or only presure due to sea water?
            "units": "dbar",
        },
    ),
    "O2sol": {
        "units": "umol/kg",
    },
    "O2sol_SP_pt": {
        "units": "umol/kg",
    },
    "SAAR": {
        "units": "1",
    },
    "SA_freezing_from_CT": {
        "units": "g/kg",
    },
    "SA_freezing_from_CT_poly": {
        "units": "g/kg",
    },
    "SA_freezing_from_t": {
        "units": "g/kg",
    },
    "SA_freezing_from_t_poly": {
        "units": "g/kg",
    },
    "SA_from_SP": {
        "standard_name": "sea_water_absolute_salinity",
        "units": "g/kg",
    },
    "SA_from_SP_Baltic": {
        "standard_name": "sea_water_absolute_salinity",
        "units": "g/kg",
    },
    "SA_from_Sstar": {
        "standard_name": "sea_water_absolute_salinity",
        "units": "g/kg",
    },
    "SA_from_rho": {
        "standard_name": "sea_water_absolute_salinity",
        "units": "g/kg",
    },
    "SP_from_C": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_from_SA": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_from_SA_Baltic": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_from_SK": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_from_SR": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_from_Sstar": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SP_salinometer": {
        "standard_name": "sea_water_practical_salinity",
        "units": "1",
        "reference_scale": "PSS-78",
    },
    "SR_from_SP": {
        "standard_name": "sea_water_reference_salinity",
        "units": "g/kg",
    },
    "Sstar_from_SA": {
        "standard_name": "sea_water_preformed_salinity",
        "units": "g/kg",
    },
    "Sstar_from_SP": {
        "standard_name": "sea_water_preformed_salinity",
        "units": "g/kg",
    },
    "Turner_Rsubrho": (
        {
            "units": "arcdeg",
        },
        {
            "units": "1",
        },
        {
            "standard_name": "sea_water_pressure",  # Not sure (is it tot pressure or only presure due to sea water?
            "units": "dbar",
        },
    ),
    "adiabatic_lapse_rate_from_CT": {
        "units": "K/Pa",
    },
    "adiabatic_lapse_rate_ice": {
        "units": "K/Pa",
    },
    "alpha": {
        "units": "1/K",
    },
    "alpha_on_beta": {
        "units": "kg g^-1 K^-1",
    },
    "alpha_wrt_t_exact": {
        "units": "1/K",
    },
    "alpha_wrt_t_ice": {
        "units": "1/K",
    },
    "beta": {
        "units": "kg/g",
    },
    "beta_const_t_exact": {
        "units": "kg/g",
    },
    "cabbeling": {
        "units": "1/(K^2)",
    },
    "chem_potential_water_ice": {
        "units": "J/kg",
    },
    "chem_potential_water_t_exact": {
        "units": "J/g",
    },
    "cp_ice": {
        "units": "J/(kg*K)",
    },
    "cp_t_exact": {
        "units": "J/(kg*K)",
    },
    "deltaSA_atlas": {
        "units": "g/kg",
    },
    "deltaSA_from_SP": {
        "units": "g/kg",
    },
    "dilution_coefficient_t_exact": {
        "units": "(J/kg)(kg/g)",
    },
    "distance": {
        "units": "m",
    },
    "dynamic_enthalpy": {
        "units": "J/kg",
    },
    "enthalpy": {
        "units": "J/kg",
    },
    "enthalpy_CT_exact": {
        "units": "J/kg",
    },
    "enthalpy_diff": {
        "units": "J/kg",
    },
    "enthalpy_first_derivatives": (
        {
            "units": "J/(kg (g/kg))",
        },
        {
            "units": "J/(kg K)",
        },
    ),
    "enthalpy_first_derivatives_CT_exact": (
        {
            "units": "J/(kg (g/kg))",
        },
        {
            "units": "J/(kg K)",
        },
    ),
    "enthalpy_ice": {
        "units": "J/kg",
    },
    "enthalpy_second_derivatives": (
        {
            "units": "(J/kg)(g/kg)^-2",
        },
        {
            "units": "J/(kg K(g/kg))",
        },
        {
            "units": "J/(kg K^2)",
        },
    ),
    "enthalpy_second_derivatives_CT_exact": (
        {
            "units": "(J/kg)(g/kg)^-2",
        },
        {
            "units": "J/(kg K(g/kg))",
        },
        {
            "units": "J/(kg K^2)",
        },
    ),
    "enthalpy_t_exact": {
        "units": "J/kg",
    },
    "entropy_first_derivatives": (
        {
            "units": "J/(kg K(g/kg))",
        },
        {
            "units": "J/(kg K^2)",
        },
    ),
    "entropy_from_CT": {
        "units": "J/(kg*K)",
    },
    "entropy_from_pt": {
        "units": "J/(kg*K)",
    },
    "entropy_from_t": {
        "units": "J/(kg*K)",
    },
    "entropy_ice": {
        "units": "J/(kg*K)",
    },
    "entropy_second_derivatives": (
        {
            "units": "J/(kg K^3)",
        },
        {
            "units": "J/(kg (g/kg) K^2)",
        },
        {
            "units": "J/(kg K^3)",
        },
    ),
    "f": {
        "standard_name": "coriolis_parameter",
        "units": "radians/s",
    },
    "frazil_properties": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "frazil_properties_potential": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "frazil_properties_potential_poly": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "frazil_ratios_adiabatic": (
        {
            "units": "g/(kg K)",
        },
        {
            "units": "g/(kg Pa)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "frazil_ratios_adiabatic_poly": (
        {
            "units": "g/(kg K)",
        },
        {
            "units": "g/(kg Pa)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "geo_strf_dyn_height": {
        "units": "m^2/s^2",
    },
    "geostrophic_velocity": (
        {
            "units": "m/s",
        },
        {
            "units": "degree_east",
        },
        {
            "units": "degree_north",
        },
    ),
    "gibbs_ice_part_t": {
        "units": "J/kg/K",
    },
    "gibbs_ice_pt0": {
        "units": "J/kg/K",
    },
    "gibbs_ice_pt0_pt0": {
        "units": "J/kg/K^2",
    },
    "grav": {
        "units": "m/s^2",
    },
    "ice_fraction_to_freeze_seawater": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "internal_energy": {
        "units": "J/kg",
    },
    "internal_energy_ice": {
        "units": "J/kg",
    },
    "kappa": {
        "units": "1/Pa",
    },
    "kappa_const_t_ice": {
        "units": "1/Pa",
    },
    "kappa_ice": {
        "units": "1/Pa",
    },
    "kappa_t_exact": {
        "units": "1/Pa",
    },
    "latentheat_evap_CT": {
        "units": "J/kg",
    },
    "latentheat_evap_t": {
        "units": "J/kg",
    },
    "latentheat_melting": {
        "units": "J/kg",
    },
    "melting_ice_SA_CT_ratio": {
        "units": "g/(kg K)",
    },
    "melting_ice_SA_CT_ratio_poly": {
        "units": "g/(kg K)",
    },
    "melting_ice_equilibrium_SA_CT_ratio": {
        "units": "g/(kg K)",
    },
    "melting_ice_equilibrium_SA_CT_ratio_poly": {
        "units": "g/(kg K)",
    },
    "melting_ice_into_seawater": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "melting_seaice_SA_CT_ratio": {
        "units": "g/(kg K)",
    },
    "melting_seaice_SA_CT_ratio_poly": {
        "units": "g/(kg K)",
    },
    "melting_seaice_equilibrium_SA_CT_ratio": {
        "units": "g/(kg K)",
    },
    "melting_seaice_equilibrium_SA_CT_ratio_poly": {
        "units": "g/(kg K)",
    },
    "melting_seaice_into_seawater": (
        {
            "units": "g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
    ),
    "p_from_z": {
        "standard_name": "sea_water_pressure",
        "units": "dbar",
    },
    "pot_enthalpy_from_pt_ice": {
        "units": "J/kg",
    },
    "pot_enthalpy_from_pt_ice_poly": {
        "units": "J/kg",
    },
    "pot_enthalpy_ice_freezing": {
        "units": "J/kg",
    },
    "pot_enthalpy_ice_freezing_first_derivatives": (
        {
            "units": "(J/kg)/(g/kg)",
        },
        {
            "units": "(J/kg)/Pa",
        },
    ),
    "pot_enthalpy_ice_freezing_first_derivatives_poly": (
        {
            "units": "(J/kg)/(g/kg)",
        },
        {
            "units": "(J/kg)/Pa",
        },
    ),
    "pot_enthalpy_ice_freezing_poly": {
        "units": "J/kg",
    },
    "pot_rho_t_exact": {
        "standard_name": "sea_water_potential_density",
        "units": "kg/m^3",
    },
    "pressure_coefficient_ice": {
        "units": "Pa/K",
    },
    "pressure_freezing_CT": {
        "units": "dbar",
    },
    "pt0_from_t": {
        "standard_name": "sea_water_potential_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt0_from_t_ice": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_first_derivatives": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "1",
        },
    ),
    "pt_from_CT": {
        "standard_name": "sea_water_potential_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_from_entropy": {
        "standard_name": "sea_water_potential_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_from_pot_enthalpy_ice": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_from_pot_enthalpy_ice_poly": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_from_t": {
        "standard_name": "sea_water_potential_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_from_t_ice": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "pt_second_derivatives": (
        {
            "units": "K/((g/kg)^2)",
        },
        {
            "units": "1/(g/kg)",
        },
        {
            "units": "1/K",
        },
    ),
    "rho": {
        "standard_name": "sea_water_density",
        "units": "kg m^-3",
    },
    "rho_alpha_beta": (
        {
            "units": "kg/m^3",
        },
        {
            "units": "1/K",
        },
        {
            "units": "kg/g",
        },
    ),
    "rho_first_derivatives": (
        {
            "units": "(kg/m^3)(g/kg)^-1",
        },
        {
            "units": "kg/(m^3 K)",
        },
        {
            "units": "kg/(m^3 Pa)",
        },
    ),
    "rho_first_derivatives_wrt_enthalpy": (
        {
            "units": "(kg/m^3)(g/kg)^-1",  # matlab doc is uncorrect
        },
        {
            "units": "(kg/m^3)(J/kg)^-1",
        },
    ),
    "rho_ice": {
        "units": "kg/m^3",
    },
    "rho_second_derivatives": (
        {
            "units": "(kg/m^3)(g/kg)^-2",
        },
        {
            "units": "(kg/m^3)(g/kg)^-1 K^-1",
        },
        {
            "units": "(kg/m^3) K^-2",
        },
        {
            "units": "(kg/m^3)(g/kg)^-1 Pa^-1",
        },
        {
            "units": "(kg/m^3) K^-1 Pa^-1",
        },
    ),
    "rho_second_derivatives_wrt_enthalpy": (
        {
            "units": "(kg/m^3)(g/kg)^-2",  # matlab doc is uncorrect
        },
        {
            "units": "(kg/m^3)(g/kg)^-1 J^-1/kg^-1",
        },
        {
            "units": "(kg/m^3)(J/kg)^-2",
        },
    ),
    "rho_t_exact": {
        "standard_name": "sea_water_density",
        "units": "kg/m^3",
    },
    "seaice_fraction_to_freeze_seawater": (
        {
            "units": " g/kg",
        },
        {
            "units": "degC",
            "reference_scale": "ITS-90",
        },
        {
            "units": "1",
        },
    ),
    "sigma0": {
        "standard_name": "sea_water_sigma_t",
        "units": "kg/m^3",
    },
    "sigma1": {
        "units": "kg/m^3",
    },
    "sigma2": {
        "units": "kg/m^3",
    },
    "sigma3": {
        "units": "kg/m^3",
    },
    "sigma4": {
        "units": "kg/m^3",
    },
    "sound_speed": {
        "standard_name": "speed_of_sound_in_sea_water",
        "units": "m/s",
    },
    "sound_speed_ice": {
        "units": "m/s",
    },
    "sound_speed_t_exact": {
        "standard_name": "speed_of_sound_in_sea_water",
        "units": "m/s",
    },
    "specvol": {
        "units": "m^3/kg",
    },
    "specvol_alpha_beta": (
        {
            "units": "m^3/kg",
        },
        {
            "units": "1/K",
        },
        {
            "units": "kg/g",
        },
    ),
    "specvol_anom_standard": {
        "units": "m^3/kg",
    },
    "specvol_first_derivatives": (
        {
            "units": "(m^3/kg)(g/kg)^-1",
        },
        {
            "units": "m^3/(kg K)",
        },
        {
            "units": "m^3/(kg Pa)",
        },
    ),
    "specvol_first_derivatives_wrt_enthalpy": (
        {
            "units": "(m^3/kg)(g/kg)^-1",  # seems to be an error in the doc
        },
        {
            "units": "(m^3/kg)(J/kg)^-1",
        },
    ),
    "specvol_ice": {
        "units": "m^3/kg",
    },
    "specvol_second_derivatives": (
        {
            "units": "(m^3/kg)(g/kg)^-2",
        },
        {
            "units": "(m^3/kg)(g/kg)^-1 K^-1",
        },
        {
            "units": "(m^3/kg) K^-2",
        },
        {
            "units": "(m^3/kg)(g/kg)^-1 Pa^-1",  # seems to be an error in the doc
        },
        {
            "units": "(m^3/kg) K^-1 Pa^-1",
        },
    ),
    "specvol_second_derivatives_wrt_enthalpy": (
        {
            "units": "(m^3/kg)(g/kg)^-2",  # error in doc?
        },
        {
            "units": "(m^3/kg)(g/kg)^-1 J^-1/kg^-1",
        },
        {
            "units": "(m^3/kg)(J/kg)^-2",
        },
    ),
    "specvol_t_exact": {
        "units": "kg/m^3",
    },
    "spiciness0": {
        "units": "kg/m^3",
    },
    "spiciness1": {
        "units": "kg/m^3",
    },
    "spiciness2": {
        "units": "kg/m^3",
    },
    "t90_from_t68": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "t_deriv_chem_potential_water_t_exact": {
        "units": "J/g/C",
    },
    "t_freezing": {
        "standard_name": "freezing_temperature_of_sea_water",  # Not sure
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "t_freezing_first_derivatives": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "t_freezing_first_derivatives_poly": (
        {
            "units": "K/(g/kg)",
        },
        {
            "units": "K/Pa",
        },
    ),
    "t_freezing_poly": {
        "standard_name": "freezing_temperature_of_sea_water",  # Not sure
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "t_from_CT": {
        "standard_name": "sea_water_temperature",
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "t_from_pt0_ice": {
        "units": "degC",
        "reference_scale": "ITS-90",
    },
    "thermobaric": {
        "units": "1/(K Pa)",
    },
    "z_from_p": {
        "standard_name": "height_above_mean_sea_level",
        "units": "m",
    },
}
