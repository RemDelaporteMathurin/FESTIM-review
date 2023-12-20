import numpy as np
from festim import k_B


# ##### Tungsten ######
#
# Taken from (P.Tolias, 2017)


def Cp_W(T):  # units in J/(kg*K)
    return (
        21.868372
        + 8.068661e-03 * T
        - 1e-06 * T**2
        + 1.075862e-09 * T**3
        + 1.406637e04 / T**2
    )


def rho_W(T):  # units in kg/m**3
    """
    (adjusted by factor 1000 as orginial equation in g/cm**3)
    """
    T_W_0 = 273.15
    return (
        19250
        - 2.66207e-01 * (T - T_W_0)
        - 3.0595e-06 * (T - T_W_0) ** 2
        - 9.5185e-09 * (T - T_W_0) ** 3
    )


def thermal_cond_W(T):  # units in W/(m*K)
    return (
        149.441
        - 45.466e-03 * T
        + 13.193e-06 * T**2
        - 1.484e-09 * T**3
        + 3.866e06 / (T + 1) ** 2
    )
    # (T+1) is there to avoid dividing by 0


# taken from (Frauenfelder, R. 1969)
D_0_W = 4.1e-7  # Diffusivity pre-exponential factor (m^(2).s^(-1))
E_D_W = 0.39  # Diffusivity activation energy (eV)
S_0_W = 1.87e24  # Solubility pre-exponential factor (m^(-3).Pa^(-0.5))
E_S_W = 1.04  # Solutbiility activation energy (eV)

atom_density_W = 6.3222e28


def D_W(T):
    return D_0_W * np.exp(-E_D_W / k_B / T)


def S_W(T):
    return S_0_W * np.exp(-E_S_W / k_B / T)


# ##### EUROfer ######
#   Values taken from Materials properties handbook


def Cp_eurofer(T):  # units in J/(kg*K)
    return -139.66 + 3.4777 * T - 0.0063847 * T**2 + 4.0984e-06 * T**3


def rho_eurofer(T):  # units in kg/m**3
    return 7852.102143 - 0.331026405 * T


def thermal_cond_eurofer(T):  # units in W/(m*K)
    return 5.4308 + 0.13565 * T - 2.3862e-04 * T**2 + 1.3393e-07 * T**3


# taken from (Chen, 2021)
D_0_eurofer = 3.15e-08  # Diffusivity pre-exponential factor (m2/s)
E_D_eurofer = 0.0622  # Diffusivity activation energy (eV)
S_0_eurofer = 2.4088e23  # Solubility pre-exponential factor (atom/m3 Pa^-0.5)
E_S_eurofer = 0.3026  # Solutbiility activation energy (eV)

atom_density_eurofer = 8.409e28  # (m-3)
trap_density_eurofer = 4.5e23  # (m-3)
trap_energy_eurofer = 0.7804  # (eV)

# recombination coefficient from Liu Journal of Nuclear Materials (2021)
Kr_0_eurofer = 1.4143446334700682e-26
E_Kr_eurofer = -0.25727457261201786


def D_eurofer(T):
    return D_0_eurofer * np.exp(-E_D_eurofer / k_B / T)


def S_eurofer(T):
    return S_0_eurofer * np.exp(-E_S_eurofer / k_B / T)


# ##### LiPi ######
#
#  Values taken from (D.Martelli et al, 2019)


def Cp_lipb(T):  # units in J/(kg*K)
    """
    adjusted by factor 1000 as orginial equation in J/(g*K)
    for values of temperature 508K < T < 800K,
    """
    return 195 - 9.116e-03 * T


def rho_lipb(T):  # units in kg/(m**3)
    return 10520.35 - 1.19051 * T


def thermal_cond_lipb(T):  # units in W/(m*K)
    """
    adjusted by factor 100 as original equation in W/(cm*K))
    """
    return 9.14779235 + 0.019631 * T


def visc_lipb(T):  # units (Pa s)
    return (
        0.01555147189
        - 4.827051855e-05 * T
        + 5.641475215e-08 * T**2
        - 2.2887e-11 * T**3
    )


def beta_lipb(T):  # units in K-1
    return 1.1221e-04 + 1.531e-08 * T


rho_0_lipb = 9808.2464435  # value T = 300K, units in kg/(m**3)

# taken from (Reiter, 1990)
D_0_lipb = 4.03e-08  # Diffusivity coefficient pre-exponential factor
E_D_lipb = 0.2021  # Diffusivity coefficient activation energy (eV)

# taken from (Aiello, 2008)
S_0_lipb = 1.427214e23  # Solubility coefficient pre-exponential factor
E_S_lipb = 0.133  # Solutbiility coefficient activation energy (eV)


def D_lipb(T):
    return D_0_lipb * np.exp(-E_D_lipb / k_B / T)


def S_lipb(T):
    return S_0_lipb * np.exp(-E_S_lipb / k_B / T)


