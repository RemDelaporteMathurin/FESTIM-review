import numpy as np

# atom_density  =  density(g/m3)*Na(/mol)/M(g/mol)
atom_density_W = 6.3222e28  # atomic density m^-3
atom_density_Cu = 8.4912e28  # atomic density m^-3
atom_density_CuCrZr = 2.6096e28  # atomic density m^-3


def polynomial(coeffs, x, main):
    val = coeffs[0]
    for i in range(1, 4):
        if main:
            val += coeffs[i] * np.float_power(x, i)
        else:
            val += coeffs[i] * x**i
    return val


def rhoCp_W(T, main=False):
    coeffs = [2.48160e6, 5.98312e2, -8.30703e-2, 5.15356e-6]
    return polynomial(coeffs, T, main=main)


def thermal_cond_W(T, main=False):
    coeffs = [1.75214e2, -1.07335e-1, 5.03006e-5, -7.84154e-9]
    return polynomial(coeffs, T, main=main)


def rhoCp_Cu(T, main=False):
    coeffs = [3.45899e6, 4.67353e2, 6.14079e-2, 1.68402e-4]
    return polynomial(coeffs, T, main=main)


def thermal_cond_Cu(T, main=False):
    coeffs = [4.02301e02, -7.88669e-02, 3.76147e-05, -3.93153e-08]
    return polynomial(coeffs, T, main=main)


def rhoCp_CuCrZr(T, main=False):
    coeffs = [3.46007e6, 6.22091e2, 1.51383e-1, -1.79134e-4]
    return polynomial(coeffs, T, main=main)


def thermal_cond_CuCrZr(T, main=False):
    coeffs = [3.12969e2, 2.57678e-01, -6.45110e-4, 5.25780e-7]
    return polynomial(coeffs, T, main=main)
