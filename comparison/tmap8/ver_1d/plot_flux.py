import numpy as np
import matplotlib.pyplot as plt

data_festim = np.genfromtxt("results/permeation_flux.csv", delimiter=",", names=True)
data_tmap8 = np.genfromtxt("ver-1d-diffusion_out.csv", delimiter=",", names=True)

t_analytic = np.linspace(0.01, 10, num=500)


def exact_flux(t: np.array):
    N = 3.1622e22
    scale = 1e-4 * N
    c_0 = 1e-4 * N / scale
    l = 1
    T = 1000
    D = 1
    k = 1e15 / (N / scale)
    p = 1e13 * np.exp(-100 / T)
    n = 0.1 * N / scale
    trap_parameter = p / (k * n) + c_0 / n
    # print(trap_parameter)
    # print(c_0 / n)
    D_eff = D / (1 + 1 / trap_parameter)

    m = np.vstack((np.arange(1, 10000),) * t.size)
    summation = (-1) ** m * np.exp(-(m**2) * np.pi**2 * D_eff * t[:, None] / l**2)
    summation = np.sum(summation, axis=1)

    val = c_0 * D / l * (1 + 2 * summation)
    return val


flux_festim = -data_festim["Flux_surface_2_solute"]
flux_tmap8 = data_tmap8["outflux"]

t_festim = data_festim["ts"]
t_tmap8 = data_tmap8["time"]

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

plt.sca(axs[0])

plt.fill_between(
    t_analytic, 0, exact_flux(t_analytic), label="exact solution", alpha=0.2
)
(l_festim,) = plt.plot(t_festim, flux_festim, label="FESTIM")
(l_tmap8,) = plt.plot(t_tmap8, flux_tmap8, label="TMAP8", linestyle="dashed")
plt.ylabel("Hydrogen flux")
plt.legend()
plt.ylim(bottom=0)

plt.sca(axs[1])

idx_tmap = np.where(flux_tmap8 > 1e-4)
idx_festim = np.where(flux_festim > 1e-4)
plt.plot(
    t_festim[idx_festim],
    flux_festim[idx_festim] / exact_flux(t_festim[idx_festim]),
    label="FESTIM",
    color=l_festim.get_color(),
)
plt.plot(
    t_tmap8[idx_tmap],
    flux_tmap8[idx_tmap] / exact_flux(t_tmap8[idx_tmap]),
    label="TMAP8",
    linestyle="dashed",
    color=l_tmap8.get_color(),
)
plt.ylabel("$J_\mathrm{computed}/J_\mathrm{analytical}$")
plt.xlabel("Time")
plt.ylim(bottom=1)

festim_error = ((flux_festim[1:] - exact_flux(t_festim[1:])) ** 2).mean()
tmap_error = ((flux_tmap8[1:] - exact_flux(t_tmap8[1:])) ** 2).mean()

print(f"MSE FESTIM: {festim_error:.2e}")
print(f"MSE TMAP8 : {tmap_error:.2e}")
for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"ver-1d-results.{ext}")
plt.show()
