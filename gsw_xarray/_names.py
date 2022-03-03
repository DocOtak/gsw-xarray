_names = {
    "CT_first_derivatives": ("CT_SA", "CT_pt"),
    "CT_first_derivatives_wrt_t_exact": ("CT_SA_wrt_t", "CT_T_wrt_t", "CT_P_wrt_t"),
    "CT_freezing": "CT_freezing",
    "CT_freezing_first_derivatives": ("CTfreezing_SA", "CTfreezing_P"),
    "CT_freezing_first_derivatives_poly": ("CTfreezing_SA", "CTfreezing_P"),
    "CT_freezing_poly": "CT_freezing",
    "CT_from_enthalpy": "CT",
    "CT_from_enthalpy_exact": "CT",
    "CT_from_entropy": "CT",
    "CT_from_pt": "CT",
    "CT_from_rho": ("CT", "CT"),
    "CT_from_t": "CT",
    "CT_maxdensity": "CT",
    "CT_second_derivatives": ("CT_SA_SA", "CT_SA_pt", "CT_pt_pt"),
    "C_from_SP": "C",
    "Fdelta": "Fdelta",
    "Helmholtz_energy_ice": "Helmholtz_energy_ice",
    "Hill_ratio_at_SP2": "Hill_ratio",
    "IPV_vs_fNsquared_ratio": ("IPV_vs_fNsquared_ratio", "p_mid"),
    "Nsquared": ("N2", "p_mid"),
    "O2sol": "O2sol",
    "O2sol_SP_pt": "O2sol",
    "SAAR": "SAAR",
    "SA_freezing_from_CT": "SA",
    "SA_freezing_from_CT_poly": "SA",
    "SA_freezing_from_t": "SA",
    "SA_freezing_from_t_poly": "SA",
    "SA_from_SP": "SA",
    "SA_from_SP_Baltic": "SA",
    "SA_from_Sstar": "SA",
    "SA_from_rho": "SA",
    "SP_from_C": "SP",
    "SP_from_SA": "SP",
    "SP_from_SA_Baltic": "SP",
    "SP_from_SK": "SP",
    "SP_from_SR": "SP",
    "SP_from_Sstar": "SP",
    "SP_salinometer": "SP",
    "SR_from_SP": "SR",
    "Sstar_from_SA": "Sstar",
    "Sstar_from_SP": "Sstar",
    "Turner_Rsubrho": ("Tu", "Rsubrho", "p_mid"),
    "adiabatic_lapse_rate_from_CT": "adiabatic",
    "adiabatic_lapse_rate_ice": "adiabatic",
    "alpha": "alpha",
    "alpha_on_beta": "alpha",
    "alpha_wrt_t_exact": "alpha",
    "alpha_wrt_t_ice": "alpha",
    "beta": "beta",
    "beta_const_t_exact": "beta",
    "cabbeling": "cabbeling",
    "chem_potential_water_ice": "chem",
    "chem_potential_water_t_exact": "chem",
    "cp_ice": "cp",
    "cp_t_exact": "cp",
    "deltaSA_atlas": "deltaSA",
    "deltaSA_from_SP": "deltaSA",
    "dilution_coefficient_t_exact": "dilution_coefficient",
    "distance": "distance",
    "dynamic_enthalpy": "dynamic_enthalpy",
    "enthalpy": "enthalpy",
    "enthalpy_CT_exact": "enthalpy",
    "enthalpy_diff": "enthalpy",
    "enthalpy_first_derivatives": ("h_SA", "h_CT"),
    "enthalpy_first_derivatives_CT_exact":  ("h_SA", "h_CT"), # difference with matlab code that return 3 outputs
    "enthalpy_ice": "enthalpy_ice",
    "enthalpy_second_derivatives": ("h_SA_SA", "h_SA_CT", "h_CT_CT"),
    "enthalpy_second_derivatives_CT_exact": ("h_SA_SA", "h_SA_CT", "h_CT_CT"),
    "enthalpy_t_exact": "enthalpy",
    "entropy_first_derivatives": ("eta_SA", "eta_CT"),
    "entropy_from_CT": "entropy",
    "entropy_from_pt": "entropy",
    "entropy_from_t": "entropy",
    "entropy_ice": "entropy",
    "entropy_second_derivatives": ("eta_SA_SA", "eta_SA_CT", "eta_CT_CT"),
    "f": "f",
    "frazil_properties": ("SA_final", "CT_final", "w_Ih_final"),
    "frazil_properties_potential": ("SA_final", "CT_final", "w_Ih_final"),
    "frazil_properties_potential_poly": ("SA_final", "CT_final", "w_Ih_final"),
    "frazil_ratios_adiabatic": ("dSA_dCT_frazil", "dSA_dP_frazil", "dCT_dP_frazil"),
    "frazil_ratios_adiabatic_poly": ("dSA_dCT_frazil", "dSA_dP_frazil", "dCT_dP_frazil"),
    "geo_strf_dyn_height": "dynamic_height",
    "geostrophic_velocity": ("geostrophic_velocity", "mid_lon", "mid_lat"),
    "gibbs_ice_part_t": "gibbs_ice_part_t",
    "gibbs_ice_pt0": "gibbs_ice_part_pt0",
    "gibbs_ice_pt0_pt0": "gibbs_ice_pt0_pt0",
    "grav": "grav",
    "ice_fraction_to_freeze_seawater": ("SA_freeze", "CT_freeze", "w_Ih"),
    "internal_energy": "internal_energy",
    "internal_energy_ice": "internal_energy_ice",
    "kappa": "kappa",
    "kappa_const_t_ice": "kappa_const_t_ice",
    "kappa_ice": "kappa_ice",
    "kappa_t_exact": "kappa_t_exact",
    "latentheat_evap_CT": "latentheat_evap",
    "latentheat_evap_t": "latentheat_evap",
    "latentheat_melting": "latentheat_melting",
    "melting_ice_SA_CT_ratio": "melting_ice_SA_CT_ratio",
    "melting_ice_SA_CT_ratio_poly": "melting_ice_SA_CT_ratio",
    "melting_ice_equilibrium_SA_CT_ratio": "melting",
    "melting_ice_equilibrium_SA_CT_ratio_poly": "melting",
    "melting_ice_into_seawater": ("SA", "CT", "w_Ih_final"),
    "melting_seaice_SA_CT_ratio": "melting_seaice_SA_CT_ratio",
    "melting_seaice_SA_CT_ratio_poly": "melting_seaice_SA_CT_ratio",
    "melting_seaice_equilibrium_SA_CT_ratio": "melting_seaice_equilibrium_SA_CT_ratio",
    "melting_seaice_equilibrium_SA_CT_ratio_poly": "melting_seaice_equilibrium_SA_CT_ratio",
    "melting_seaice_into_seawater": ("SA", "CT"),
    "p_from_z": "p",
    "pchip_interp": "",
    "pot_enthalpy_from_pt_ice": "pot",
    "pot_enthalpy_from_pt_ice_poly": "pot",
    "pot_enthalpy_ice_freezing": "pot",
    "pot_enthalpy_ice_freezing_first_derivatives": "pot",
    "pot_enthalpy_ice_freezing_first_derivatives_poly": "",
    "pot_enthalpy_ice_freezing_poly": "pot",
    "pot_rho_t_exact": "pot",
    "pressure_coefficient_ice": "pressure",
    "pressure_freezing_CT": "pressure",
    "pt0_from_t": "pt0",
    "pt0_from_t_ice": "pt0",
    "pt_first_derivatives": "pt",
    "pt_from_CT": "pt",
    "pt_from_entropy": "pt",
    "pt_from_pot_enthalpy_ice": "pt0",
    "pt_from_pot_enthalpy_ice_poly": "pt0",
    "pt_from_t": "pt",
    "pt_from_t_ice": "pt",
    "pt_second_derivatives": "pt",
    "rho": "rho",
    "rho_alpha_beta": "rho",
    "rho_first_derivatives": "rho",
    "rho_first_derivatives_wrt_enthalpy": "rho",
    "rho_ice": "rho",
    "rho_second_derivatives": "rho",
    "rho_second_derivatives_wrt_enthalpy": "rho",
    "rho_t_exact": "rho",
    "seaice_fraction_to_freeze_seawater": "",
    "sigma0": "sigma0",
    "sigma1": "sigma1",
    "sigma2": "sigma2",
    "sigma3": "sigma3",
    "sigma4": "sigma4",
    "sound_speed": "sound_speed",
    "sound_speed_ice": "sound",
    "sound_speed_t_exact": "sound_speed",
    "specvol": "specvol",
    "specvol_alpha_beta": "specvol",
    "specvol_anom_standard": "specvol",
    "specvol_first_derivatives": "v",
    "specvol_first_derivatives_wrt_enthalpy": "v",
    "specvol_ice": "specvol",
    "specvol_second_derivatives": "v",
    "specvol_second_derivatives_wrt_enthalpy": "v",
    "specvol_t_exact": "specvol",
    "spiciness0": "",
    "spiciness1": "",
    "spiciness2": "",
    "t90_from_t68": "t90",
    "t_deriv_chem_potential_water_t_exact": "chem",
    "t_freezing": "t",
    "t_freezing_first_derivatives": "tfreezing",
    "t_freezing_first_derivatives_poly": "tfreezing",
    "t_freezing_poly": "t",
    "t_from_CT": "temperature",
    "t_from_pt0_ice": "t",
    "thermobaric": "thermobaric",
    "z_from_p": "z",
}
