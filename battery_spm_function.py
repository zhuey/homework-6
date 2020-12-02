import numpy as np
from math import exp

# Constants
F = 96485
R = 8.3145
sigma = 5.670e-8

def residual(t, SV, pars, ptr, flags):


    " ===================== ANODE ====================="
    RTinv = 1/R/SV[ptr.T_an]
    dSV_dt = np.zeros_like(SV)
    
    # Double layer potential:
    eta_an = SV[ptr.phi_an] - pars.dPhi_eq_an
    i_Far_an = pars.i_o_an*(exp(-pars.n_an*F*pars.beta_an*eta_an*RTinv)
                      - exp(pars.n_an*F*(1-pars.beta_an)*eta_an*RTinv))
    i_dl_an = pars.i_ext*pars.A_fac_an - i_Far_an
    dSV_dt[ptr.phi_an] = -i_dl_an*pars.C_dl_an_inv

    # Anode Temperature:

    # arrays have species ordered as: Li_an, Li+_elyte, electron:
    # Molar production rate (mol/m3/s)
    sdot_k = np.array([i_Far_an/F/pars.A_fac_an, -i_Far_an/F/pars.A_fac_an,     
        -i_Far_an/F/pars.A_fac_an])/pars.H_an
    # Species enthalpies (J/mol)
    h_k = np.array([pars.h_Li_an, pars.h_Li_elyte, 0.])
    # Total species energy: h + z_k*F*Phi
    energy_k = h_k + np.array([0, 0, -F*SV[ptr.phi_an]])

    # 1/distance betwen center of anode and center of separator
    dyInv_an = 1/(0.5*pars.H_an + 0.5*pars.H_elyte)
    # Volume-weighted thermal conductivity between center of anode and center 
    # of separator 
    lambda_an = (0.5*(pars.H_an*pars.lambda_cond_an + 
        pars.H_elyte*pars.lambda_cond_elyte)*dyInv_an)

    """ 
    YOUR CODE GOES HERE (PART I)
    
    CALCULATE TERMS FOR VOLUMETRIC THERMAL ENERGY PRODUCTION (W/m3)
    """
    # Conduction heat transfer from the anode to the electrolyte separator:
    Q_cond_an = 0

    # Volumetric heat source/sink terms: (W/m3)
    Q_rxn = 0
    Q_ohm_el = 0
    Q_ohm_io = 0
    Q_cond = 0
    Q_rad = 0
    Q_conv = 0
    """
    END CODING
    """

    dSV_dt[ptr.T_an] = pars.RhoCpInv_an*(flags.rad*Q_rad + flags.cond*Q_cond 
        + flags.ohm_el*Q_ohm_el + flags.ohm_io*Q_ohm_io + flags.rxn*Q_rxn 
        + flags.conv*Q_conv)

    
    " ===================== ELYTE ====================="
    # 1/distance betwen center of cathode and center of separator
    dyInv_ca = 1/(0.5*pars.H_ca + 0.5*pars.H_elyte)
    # Volume-weighted thermal conductivity between center of cathode and center 
    # of separator 
    lambda_ca = (0.5*(pars.H_ca*pars.lambda_cond_ca + 
        pars.H_elyte*pars.lambda_cond_elyte)*dyInv_ca)

    """
    YOUR CODE GOES HERE (PART II)

    CALCULATE TERMS FOR VOLUMETRIC THERMAL ENERGY PRODUCTION (W/m3)
    """
    # Conduction heat transfer from the electrolyte separator to the cathode:
    Q_cond_ca = 0

    # Volumetric heat source/sink terms: (W/m3)
    Q_rxn = 0
    Q_ohm_el = 0
    Q_ohm_io = 0
    Q_cond = 0
    Q_rad = 0
    Q_conv = 0
    """
    END CODING
    """

    dSV_dt[ptr.T_elyte] = pars.RhoCpInv_elyte*(flags.rad*Q_rad 
        + flags.cond*Q_cond + flags.ohm_el*Q_ohm_el + flags.ohm_io*Q_ohm_io 
        + flags.rxn*Q_rxn + flags.conv*Q_conv)

    " ===================== CATHODE ====================="
    
    # Cathode double layer potential:
    RTinv = 1/R/SV[ptr.T_ca]
    eta_ca = SV[ptr.phi_ca] - pars.dPhi_eq_ca
    i_Far_ca = pars.i_o_ca*(exp(-pars.n_ca*F*pars.beta_ca*eta_ca*RTinv)
                      - exp(pars.n_ca*F*(1-pars.beta_ca)*eta_ca*RTinv))
    i_dl_ca = -pars.i_ext*pars.A_fac_ca - i_Far_ca
    dSV_dt[ptr.phi_ca] = -i_dl_ca*pars.C_dl_ca_inv

    # Cathode Temperature

    # arrays have species ordered as: Li_ca, Li+_elyte, electron
    # Molar production rate (mol/m3/s)
    sdot_k = np.array([i_Far_ca/F/pars.A_fac_ca, -i_Far_ca/F/pars.A_fac_ca,
        -i_Far_ca/F/pars.A_fac_ca])/pars.H_ca
    # Species enthalpies (J/mol)
    h_k = np.array([pars.h_Li_ca, pars.h_Li_elyte, 0])
    # Total species energy: h + z_k*F*Phi
    energy_k = h_k + np.array([0, 0, -F*SV[ptr.phi_ca]])

    """
    YOUR CODE GOES HERE (PART III)
    
    CALCULATE TERMS FOR VOLUMETRIC THERMAL ENERGY PRODUCTION (W/m3)
    """
    Q_rxn = 0
    Q_ohm_el = 0
    Q_ohm_io = 0
    Q_cond = 0
    Q_rad = 0
    Q_conv = 0
    """
    END CODING
    """
    dSV_dt[ptr.T_ca] = pars.RhoCpInv_ca*(flags.rad*Q_rad + flags.cond*Q_cond 
        + flags.ohm_el*Q_ohm_el + flags.ohm_io*Q_ohm_io + flags.rxn*Q_rxn 
        + flags.conv*Q_conv)

    return dSV_dt