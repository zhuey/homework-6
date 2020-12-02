from battery_spm_inputs import *
import numpy as np

# Calculate double layer initial conditions:
phi_dl_an_0 = phi_an_0 - phi_sep_0
phi_dl_ca_0 = phi_ca_0 - phi_sep_0

# Calculate the total storage capacity of each electrode, per unit area
# (specific capacity times electrode active material mass)
capacity_anode = capacity_graphite*H_an*eps_graphite*density_graphite
capacity_cathode = capacity_LCO*H_ca*eps_LCO*density_LCO
# Actual battery capacity is the minimum of these two
capacity_area = min(capacity_anode,capacity_cathode)

# Integration time is 3600 seconds per hour, divide by charges per hour.
# We multiply this by a "charge fraction," as we do not want to charge or 
# discharge the battery all the way (dPhi_eq would go to plus/minus infinity!)
t_final = charge_frac*3600./C_rate

# Initial solution vector:
SV_0 = np.array([phi_dl_an_0, T_amb, T_amb, phi_dl_ca_0, T_amb])

# Create class to point to the correct variable locations in the SV:
class ptr:
    phi_an = 0
    T_an = 1

    T_elyte = 2

    phi_ca = 3
    T_ca = 4

# Load inputs and other parameters into 'pars' class:

#Preparatory calculations that we don't want stored in 'pars':
# Volume- and mass-weighted average density and Cp, respectively:
rho_avg_an = eps_graphite*density_graphite + (1-eps_graphite)*density_elyte
massfrac_graphite = eps_graphite*density_graphite/rho_avg_an
Cp_avg_an = massfrac_graphite*Cp_graphite + (1 - massfrac_graphite)*Cp_elyte

rho_avg_ca = eps_LCO*density_LCO + (1-eps_LCO)*density_elyte
massfrac_LCO = eps_LCO*density_LCO/rho_avg_ca
Cp_avg_ca = massfrac_LCO*Cp_LCO + (1 - eps_LCO)*Cp_elyte
class pars:
    # Component thicknesses:
    H_an = H_an
    H_elyte = H_elyte
    H_ca = H_ca

    # Equilibrium double layer potentials (V)
    # Assume fixed (for now!)
    dPhi_eq_an = dPhi_eq_an
    dPhi_eq_ca = dPhi_eq_ca

    # Butler-Volmer parameters:
    i_o_an = i_o_an
    n_an = n_an
    beta_an = beta_an

    i_o_ca = i_o_ca
    n_ca = n_ca
    beta_ca = beta_ca
    
    # Double layer capacitances (F/m2)
    C_dl_an_inv = 1/C_dl_an
    C_dl_ca_inv = 1/C_dl_ca

    # Lithium enthalpies (J/mol)
    h_Li_an = h_Li_an
    h_Li_elyte = h_Li_elyte
    h_Li_ca = h_Li_ca

    # External current density:
    C_rate = C_rate
    i_ext = C_rate*capacity_area

    # Total geometric area per unit surface area:
    A_fac_an = r_p_an/3/H_an/eps_graphite
    A_fac_ca = r_p_ca/3/H_ca/eps_LCO

    # Inverse of mass density times specific heat capacity:
    RhoCpInv_an = 1/rho_avg_an/Cp_avg_an
    RhoCpInv_elyte = 1/density_elyte/Cp_elyte
    RhoCpInv_ca = 1/rho_avg_ca/Cp_avg_ca
    
    # Volume-averaged thermal conductivities:
    lambda_cond_an = (eps_graphite*lambda_cond_an 
        + (1-eps_graphite)*lambda_cond_elyte)
    lambda_cond_elyte = lambda_cond_elyte
    lambda_cond_ca = (eps_LCO*lambda_cond_ca 
        + (1-eps_LCO)*lambda_cond_elyte)

    # Electronic and ionic resistivities (ohm-m):
    R_el_an = 1/sigma_el_graphite/eps_graphite
    R_io_an = 1/sigma_io_elyte/(1-eps_graphite)
    R_io_elyte = 1/sigma_io_elyte/eps_elyte_sep
    R_io_ca = 1/sigma_io_elyte/(1-eps_LCO)
    R_el_ca = 1/sigma_el_LCO/eps_LCO

    # Emmissivity:
    emmissivity = emmissivity
    # Ambient temperature:
    T_amb = T_amb
    # Convection coefficient:
    h_conv = h_conv
    # Battery external surface area per unit volume:
    A_ext = A_ext

#