# Inputs:

C_rate = 0.1 # How many charges per hour?

T_amb = 298 # Ambient (surrounding) temnperature, K

" Microstructure and geometry "
r_p_an = 4e-6 # Anode particle radius, m
r_p_ca = 0.3e-6 # Cathode particle radius, m

H_an = 80e-6  # Anode thickness, m
H_elyte = 25e-6 # Electrolyte separator thickness, m
H_ca = 80e-6  # Cathode thickness, m

eps_graphite = .65 # Volume fraction of graphite in anode
eps_elyte_sep = 0.65 # Volume fraction of elyte in separator
eps_LCO = 0.65 # Volukme fraction of LCO phase in cathode

" Electrochemical parameters "
# Initial voltages (used to calculate phi_dl guesses)
phi_an_0 = 0 #V
phi_sep_0 = 1.8  #V
phi_ca_0 = 4.6  #V

# Equilibrium double layer potential (phi_electrode - phi_elyte)
dPhi_eq_an = 0.104

# Molar enthalpy of Li species (Li or Li+)
h_Li_an = -10e3 #J/mol
h_Li_elyte = 0 #J/mol
h_Li_ca = -3.9e5 #J/mol

C_dl_an = 1e-2 # Double layer capacitance, F/m2 of dl interface
C_dl_ca = 1e-3 # Double layer capacitance, F/m2 of dl interface

i_o_an = 4.0e-3  # Exchange current density, A/m2
n_an = 1 # Charge equivalents transfered to anode
beta_an = 0.5 # Symmetry parameter


i_o_ca = 1e-3 # Exchange current density, A/m2
n_ca = 1# Charge equivalents transfered to cathode
beta_ca = 0.5# Symmetry parameter


" Material properties "
# Anode
density_graphite = 2260 # mass density, kg/m3
capacity_graphite = 350 # Anode charge storage capacity, Ah/kg
# Cp from https://webbook.nist.gov/cgi/cbook.cgi?ID=C7782425&Mask=2
Cp_graphite = 691.67 #J/kg-K 
# Thermal conductivity from: 
# https://tfaws.nasa.gov/wp-content/uploads/TFAWS18-PT-11.pdf
lambda_cond_an = 1.4 #W/m-K
# conductivity taken as an average from:
# https://en.m.wikipedia.org/wiki/Electrical_resistivity_and_conductivity#Resistivity_of_various_materials
sigma_el_graphite = 2e4 #S/m

# Elyte separator
density_elyte = 1132 #kg/m3
# Cp from https://webbook.nist.gov/cgi/inchi?ID=C96491&Mask=2#Thermo-Condensed
Cp_elyte = 1520.52 #J/kg-K
# Thermal conductivity from: 
# https://tfaws.nasa.gov/wp-content/uploads/TFAWS18-PT-11.pdf
lambda_cond_elyte = 0.1 # W/m-K
# ionic conductivity of elte phase:
sigma_io_elyte = 1.280 #S/m

# Cathode
density_LCO = 2292   # mass density kg/m3
capacity_LCO = 175  # Cathode charge storage capacity, Ah/kg
dPhi_eq_ca = 3.92
# Cp from:
#  https://www.sciencedirect.com/science/article/abs/pii/S0021961414003784
Cp_LCO = 730.77 #J/kg-K
# Thermal conductivity from: 
# https://tfaws.nasa.gov/wp-content/uploads/TFAWS18-PT-11.pdf
lambda_cond_ca = 0.5 #W/m-K
# ELectronic conductivity:
sigma_el_LCO = 2e6 #S/m

" Heat Transfer Parameters "
# Radiation heat transfer emissivity:
emmissivity = 0.75
# Battery external surface area per unit volume:
A_ext = 1000

# Convection heat transfer coefficient:
h_conv = 32 #W/m2-K

# How deep do we want to charge/discharge?
charge_frac = 0.9