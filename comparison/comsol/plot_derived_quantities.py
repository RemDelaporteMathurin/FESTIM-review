import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

avogadro = 6.02214076e23  # mol-1

time_of_comparison = 1e6

# FESTIM data

data_festim = np.genfromtxt(
    "../../gallery/monoblock/derived_quantities.csv", delimiter=",", names=True
)
row = np.where(data_festim["ts"] == time_of_comparison)

data_total_trap_w = data_festim["Total_1_volume_6"] + data_festim["Total_2_volume_6"]
total_trap_w_festim = data_total_trap_w[row]

data_total_trap_cu = data_festim["Total_2_volume_7"]
total_trap_cu_festim = data_total_trap_cu[row]

data_total_trap_cuzr = data_festim["Total_2_volume_8"]
total_trap_cuzr_festim = data_total_trap_cuzr[row]

total_trap_tot_festim = (
    total_trap_w_festim + total_trap_cu_festim + total_trap_cuzr_festim
)

# flux_w_festim = data_festim["Flux_surface_9_solute"][row]
flux_coolant_festim = -data_festim["Flux_surface_10_solute"][row]
flux_poloidal_festim = -(
    data_festim["Flux_surface_11_solute"][row]
    + data_festim["Flux_surface_12_solute"][row]
)
flux_toroidal_festim = -data_festim["Flux_surface_13_solute"][row]

# COMSOL data
# Note: the COMSOL data is in mol/m^3, so we need to multiply by avogadro to get atoms/m^3

data_total_trap_w = np.genfromtxt("Iter3D_coms_trap_W.txt", delimiter="\t")
row = np.where(data_total_trap_w[:, 0] == time_of_comparison)
total_trap_w_comsol = data_total_trap_w[row, 1][0][0] * avogadro

data_total_trap_cu = np.genfromtxt("Iter3D_coms_trap_Cu.txt", delimiter="\t")
row = np.where(data_total_trap_cu[:, 0] == time_of_comparison)
total_trap_cu_comsol = data_total_trap_cu[row, 1][0][0] * avogadro

data_total_trap_cuzr = np.genfromtxt("Iter3D_coms_trap_CuZr.txt", delimiter="\t")
row = np.where(data_total_trap_cuzr[:, 0] == time_of_comparison)
total_trap_cuzr_comsol = data_total_trap_cuzr[row, 1][0][0] * avogadro

data_total_trap_tot = np.genfromtxt("Iter3D_coms_trap_tot.txt", delimiter="\t")
row = np.where(data_total_trap_tot[:, 0] == time_of_comparison)
total_trap_tot_comsol = data_total_trap_tot[row, 1][0][0] * avogadro

data_flux_coolant = np.genfromtxt("Iter3D_coms_fluxRec.txt", delimiter="\t")
row = np.where(data_flux_coolant[:, 0] == time_of_comparison)
flux_coolant_comsol = data_flux_coolant[row, 1][0][0] * avogadro

data_flux_toroidal = np.genfromtxt("Iter3D_coms_fluxPol.txt", delimiter="\t")
row = np.where(data_flux_toroidal[:, 0] == time_of_comparison)
flux_toroidal_comsol = data_flux_toroidal[row, 1][0][0] * avogadro


data_flux_poloidal_W = np.genfromtxt("Iter3D_coms_fluxW.txt", delimiter="\t")
row = np.where(data_flux_poloidal_W[:, 0] == time_of_comparison)
flux_poloidal_W_comsol = data_flux_poloidal_W[row, 1][0][0] * avogadro

data_flux_poloidal_Cu = np.genfromtxt("Iter3D_coms_fluxCu.txt", delimiter="\t")
row = np.where(data_flux_poloidal_Cu[:, 0] == time_of_comparison)
flux_poloidal_Cu_comsol = data_flux_poloidal_Cu[row, 1][0][0] * avogadro

data_flux_poloidal_CuCrZr = np.genfromtxt("Iter3D_coms_fluxCuZr.txt", delimiter="\t")
row = np.where(data_flux_poloidal_CuCrZr[:, 0] == time_of_comparison)
flux_poloidal_CuCrZr_comsol = data_flux_poloidal_CuCrZr[row, 1][0][0] * avogadro

flux_poloidal_comsol = (
    flux_poloidal_W_comsol + flux_poloidal_Cu_comsol + flux_poloidal_CuCrZr_comsol
)

# Plot
colour_festim = "tab:blue"
colour_comsol = "tab:orange"

fig, axs = plt.subplots(nrows=2, ncols=1)
plt.sca(axs[0])

(l_festim,) = plt.plot(
    [
        total_trap_w_festim,
        total_trap_cu_festim,
        total_trap_cuzr_festim,
        total_trap_tot_festim,
    ],
    label="FESTIM",
    marker="o",
)
l_festim.set_markerfacecolor(colors.to_rgba(colour_festim))
l_festim.set_color(colors.to_rgba(colour_festim))

plt.fill_between(
    range(4),
    [
        total_trap_w_comsol,
        total_trap_cu_comsol,
        total_trap_cuzr_comsol,
        total_trap_tot_comsol,
    ],
    facecolor="none",
    edgecolor=colour_comsol,
    label="COMSOL",
    hatch="//",
)


plt.yscale("log")
plt.ylabel("Trapped inventory (H)")
plt.xticks(range(4), ["W", "Cu", "CuZr", "Total"])

plt.sca(axs[1])

(l_festim,) = plt.plot(
    [flux_coolant_festim, flux_poloidal_festim, flux_toroidal_festim],
    label="FESTIM",
    marker="o",
)
l_festim.set_markerfacecolor(colors.to_rgba(colour_festim))
l_festim.set_color(colors.to_rgba(colour_festim))

plt.fill_between(
    range(3),
    [flux_coolant_comsol, flux_poloidal_comsol, flux_toroidal_comsol],
    facecolor="none",
    edgecolor=colour_comsol,
    label="COMSOL",
    hatch="//",
)

plt.yscale("log")
plt.ylabel("Flux (H/s)")
plt.xticks(range(3), ["Coolant", "Poloidal", "Toroidal"])

plt.legend()

for ax in axs:
    ax.grid(True, alpha=0.3)
    # remove top and right axis
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.savefig("comparison_derived_quantities.svg")
plt.savefig("comparison_derived_quantities.pdf")
plt.savefig("comparison_derived_quantities.png")

plt.show()
