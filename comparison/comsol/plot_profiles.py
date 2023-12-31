import matplotlib.pyplot as plt
import numpy as np

m_to_mm = 1e3

data_comsol_cm = np.genfromtxt(
    "mobile_concentration_profile.csv", delimiter=",", names=True
)
data_comsol_retention = np.genfromtxt(
    "inventory_profile.csv", delimiter=",", names=True
)

festim_folder_path = "../../gallery/monoblock"

data_festim_cm = np.genfromtxt(
    f"{festim_folder_path}/mobile_concentration_profile.csv", delimiter=",", names=True
)
data_festim_retention = np.genfromtxt(
    f"{festim_folder_path}/retention_profile.csv", delimiter=",", names=True
)

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

plt.sca(axs[0])
plt.plot(
    data_festim_cm["arc_length"] * m_to_mm,
    data_festim_cm["mobile_concentration"],
    label="FESTIM",
)
plt.plot(
    data_comsol_cm["arc_length"] * m_to_mm, data_comsol_cm["Color"], label="COMSOL"
)

plt.yscale("log")
plt.ylim(bottom=1e19)
plt.ylabel("Mobile concentration (m$^{-3}$)")

plt.annotate(
    "CuCrZr/Cu interface",
    (1.55, 2e21),
    (1.6, 1e22),
    arrowprops=dict(arrowstyle="->"),
)

plt.annotate("Cu/W", (2.5, 7e20), (3.25, 3e21), arrowprops=dict(arrowstyle="->"))

plt.sca(axs[1])

plt.plot(
    data_festim_retention["arc_length"] * m_to_mm,
    data_festim_retention["retention"],
    label="FESTIM",
)

plt.plot(
    data_comsol_retention["arc_length"] * m_to_mm,
    data_comsol_retention["Color"],
    label="COMSOL",
)
plt.yscale("log")
plt.ylabel("Total retention (m$^{-3}$)")
plt.xlabel("Distance from the cooling surface (mm)")
plt.ylim(bottom=1e20)
plt.legend()

for ax in axs:
    ax.grid(True, alpha=0.3)
    # remove top and right axis
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.savefig("comparison_profiles.svg")
plt.savefig("comparison_profiles.pdf")
plt.savefig("comparison_profiles.png")

plt.show()
