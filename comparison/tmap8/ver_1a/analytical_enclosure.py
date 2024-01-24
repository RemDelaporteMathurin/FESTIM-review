import numpy as np

import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/28766692/how-to-find-the-intersection-of-two-graphs/28766902#28766902

k = 1.38065e-23  # J/mol Boltzmann constant


def get_roots(L, l, alpha_max, step=0.0001):
    """Gets the roots of alpha = L / tan(alpha * l)

    Args:
        L (float): parameter L
        l (float): parameter l
        alpha_max (float): the maximum alpha to consider
        step (float, optional): the step discretising alphas.
            The smaller the step, the more accurate the roots.
            Defaults to 0.0001.

    Returns:
        np.array: array of roots
    """
    alphas = np.arange(0, alpha_max, step=step)[1:]

    f = alphas

    g = L / np.tan(alphas * l)

    # plt.plot(alphas, f, "-")
    # plt.plot(alphas, g, "-")

    idx = np.argwhere(np.diff(np.sign(f - g))).flatten()

    # remove one every other idx
    idx = idx[::2]
    # plt.plot(alphas[idx], f[idx], "ro")
    # plt.show()
    roots = alphas[idx]
    return roots


def get_roots_bis(L, alpha_max, step=0.0001):
    """Gets the roots of alpha = L / tan(alpha)

    Args:
        L (float): parameter L
        alpha_max (float): the maximum alpha to consider
        step (float, optional): the step discretising alphas.
            The smaller the step, the more accurate the roots.
            Defaults to 0.0001.

    Returns:
        np.array: array of roots
    """
    alphas = np.arange(0, alpha_max, step=step)[1:]

    f = alphas

    g = L / np.tan(alphas)

    plt.plot(alphas, f, "-")
    plt.plot(alphas, g, "-")

    idx = np.argwhere(np.diff(np.sign(f - g))).flatten()

    # remove one every other idx
    idx = idx[::2]
    plt.plot(alphas[idx], f[idx], "ro")
    plt.show()
    roots = alphas[idx]
    return roots


def analytical_expression_fractional_release_TMAP7(t, P_0, D, S, V, T, A, l):
    """
    FR = 1 - P(t) / P_0
    where P(t) is the pressure at time t and P_0 is the initial pressure

    Taken from https://inldigitallibrary.inl.gov/sites/sti/sti/4215153.pdf
    Equation 4
    Note: in the report, the expression of FR is given as P(T)/P_0, but it shown as 1 - P(t)/P_0 in the graph (Figure 1)
    Args:
        t (float, ndarray): time (s)
        P_0 (float): initial presure (Pa)
        D (float): diffusivity (m2/s)
        S (float): solubility (H/m3/Pa)
        V (float): enclosure volume (m3)
        T (float): temperature (K)
        A (float): enclosure surface area (m2)
        l (float): slab length (m)
    """
    L = S * T * A * k / V

    roots = get_roots(L=L, l=l, alpha_max=1e6, step=1)
    print(len(roots))
    roots = roots[:, np.newaxis]
    summation = np.exp(-(roots**2) * D * t) / (l * (roots**2 + L**2) + L)
    last_term = summation[-1]
    summation = np.sum(summation, axis=0)

    print(last_term / summation)
    pressure = 2 * P_0 * L * summation
    fractional_release = 1 - pressure / P_0
    return fractional_release


# FIXME this doesn't work
# taken from https://mooseframework.inl.gov/TMAP8/verification/ver-1a.html#longhurst1992verification
def analytical_expression_fractional_release_TMAP8(t, D, S, V, T, A, l):
    """
    Analytical expression for the fractional release given by TMAP4 report and TMAP8 docs
    This doesn't produce the correct analytical results presented by TMAP4 and TMAP8.
    Note, this expression isn't used in the TMAP7 V&V report.
    see https://github.com/idaholab/TMAP8/issues/75 for discussion with TMAP8 team

    Args:
        t (float, ndarray): time (s)
        D (float): diffusivity (m2/s)
        S (float): solubility (H/m3/Pa)
        V (float): enclosure volume (m3)
        T (float): temperature (K)
        A (float): enclosure surface area (m2)
        l (float): slab length (m)
    """
    phi = 1 / (k * T * S)
    L = l * A / (V * phi)
    roots = get_roots_bis(L=L, alpha_max=2000, step=3e-4)
    roots = roots[:, np.newaxis]
    sec = 1 / np.cos(roots)
    summation = (2 * L * sec - np.exp(-(roots**2) * D * t / l**2)) / (
        L * (L + 1) + roots**2
    )
    last_term = summation[-1]
    summation = np.sum(summation, axis=0)
    print(summation[0])
    print(last_term / summation)
    fractional_release = 1 - summation
    return fractional_release


def analytical_expression_flux(t, P_0, D, S, V, T, A, l):
    """
    value of the flux at the external surface (not in contact with pressure)
    J = -D * dc/dx

    Args:
        t (float, ndarray): time (s)
        P_0 (float): initial presure (Pa)
        D (float): diffusivity (m2/s)
        S (float): solubility (H/m3/Pa)
        V (float): enclosure volume (m3)
        T (float): temperature (K)
        A (float): enclosure surface area (m2)
        l (float): slab length (m)
    """
    L = S * T * A * k / V

    roots = get_roots(L=L, l=l, alpha_max=1e7, step=1)
    roots = roots[:, np.newaxis]

    summation = (np.exp(-(roots**2) * D * t) * roots) / (
        (l * (roots**2 + L**2) + L) * np.sin(roots * l)
    )
    last_term = summation[-1]
    summation = np.sum(summation, axis=0)

    print(last_term / summation)
    flux = 2 * S * P_0 * L * D * summation
    return flux


def cumulative_flux_analytical(t, P_0, D, S, V, T, A, l):
    """
    Analytical expression for the cumulative flux at the external surface (not in contact with pressure)
    integral(A D grad(c) . n dt) between 0 and t
    normalised by the initial quantity in the enclosure
    Args:
        t (float, ndarray): time (s)
        P_0 (float): initial presure (Pa)
        D (float): diffusivity (m2/s)
        S (float): solubility (H/m3/Pa)
        V (float): enclosure volume (m3)
        T (float): temperature (K)
        A (float): enclosure surface area (m2)
        l (float): slab length (m)
    """
    L = S * T * A * k / V

    roots = get_roots(L=L, l=l, alpha_max=1e7, step=1)
    roots = roots[:, np.newaxis]

    num = 1 - np.exp(-(roots**2) * D * t)
    denum = roots * np.sin(roots * l) * (l * (roots**2 + L**2) + L)
    summation = num / denum
    last_term = summation[-1]
    summation = np.sum(summation, axis=0)

    print(last_term / summation)
    cumulative_flux_val = 2 * S * P_0 * L * summation
    initial_quantity = P_0 * V / k / T
    return cumulative_flux_val * A / initial_quantity


if __name__ == "__main__":
    T = 2373
    times = np.linspace(0, 45, 1000)
    cum_flux = cumulative_flux_analytical(
        t=times,
        P_0=1e6,
        D=2.6237e-11,
        S=7.244e22 / T,
        V=5.20e-11,
        T=T,
        A=2.16e-6,
        l=3.3e-5,
    )
    FR_tmap8 = analytical_expression_fractional_release_TMAP8(
        t=times,
        D=2.6237e-11,
        S=7.244e22 / T,
        V=5.20e-11,
        T=T,
        A=2.16e-6,
        l=3.3e-5,
    )
    FR_tmap7 = analytical_expression_fractional_release_TMAP7(
        t=times,
        P_0=1e6,
        D=2.6237e-11,
        S=7.244e22 / T,
        V=5.20e-11,
        T=T,
        A=2.16e-6,
        l=3.3e-5,
    )
    FR_TMAP8 = np.genfromtxt("analytical.csv", delimiter=",", names=True)
    plt.plot(times, cum_flux, label="new formula", linewidth=3, color="tab:green")
    plt.plot(times, FR_tmap7, label="TMAP7")
    plt.plot(times, FR_tmap8, label="TMAP4/TMAP8 (equation)", color="tab:red")
    plt.scatter(
        FR_TMAP8["times"],
        FR_TMAP8["frac_rel"],
        label="TMAP8 (csv)",
        color="tab:green",
        alpha=0.5,
    )
    plt.ylabel("FR")
    plt.xlabel("Time (s)")

    plt.legend()
    plt.show()
