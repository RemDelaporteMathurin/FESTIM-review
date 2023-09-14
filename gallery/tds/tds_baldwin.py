import festim as F
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

model = F.Simulation()


vertices = np.concatenate(
    [
        np.linspace(0, 30e-9, num=100),
        np.linspace(30e-9, 1e-6, num=500),
    ]
)

model.mesh = F.MeshFromVertices(vertices)

beryllium = F.Material(id=1, D_0=8e-9, E_D=0.364, S_0=2.3e22, E_S=0.174)  # m2/s  # eV

model.materials = beryllium

be_atom_density = 1.85e6 / 9.0122 * 6.022e23  # atom/m3

trap_1 = F.Trap(
    k_0=4e12 / be_atom_density,
    E_k=beryllium.E_D,
    p_0=4e12,
    E_p=0.75,
    density=0.109 * be_atom_density,
    materials=beryllium,
)
trap_2 = F.Trap(
    k_0=4e12 / be_atom_density,
    E_k=beryllium.E_D,
    p_0=4e12,
    E_p=0.93,
    density=3.4e-2 * be_atom_density,
    materials=beryllium,
)


model.initial_conditions = [
    F.InitialCondition(field=1, value=0.73 * 0.109 * be_atom_density),
    F.InitialCondition(field=2, value=0.28 * 3.4e-2 * be_atom_density),
]

model.traps = [trap_1, trap_2]

implantation_temp = 300  # K
resting_time = 306
ramp = 0.3  # K/s
tds_time = (1000 - 300) / ramp

model.T = F.Temperature(
    value=sp.Piecewise(
        (implantation_temp, F.t < resting_time),
        (implantation_temp + ramp * (F.t - resting_time), True),
    )
)

pi = 3.14
M_D2 = 6.68e-27  # kg/H  molecular mass of D2
T_D2 = 300
pressure = 1.33e-6  # Pa

model.boundary_conditions = [
    F.FluxBC(surfaces=1, value=pressure / ((2 * pi**F.k_B * T_D2) ** 0.5), field=0),
    F.RecombinationFlux(Kr_0=3.4e-29, E_Kr=0.28, order=2, surfaces=1),
]


model.dt = F.Stepsize(
    initial_value=0.5,
    stepsize_change_ratio=1.1,
    t_stop=resting_time - 20,
    stepsize_stop_max=20,
    dt_min=1e-05,
)

model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-09,
    final_time=tds_time + resting_time,
)

list_of_derived_quantities = [
    F.TotalVolume("solute", volume=1),
    F.TotalVolume("retention", volume=1),
    F.TotalVolume("1", volume=1),
    F.TotalVolume("2", volume=1),
    F.AverageVolume("T", volume=1),
    F.HydrogenFlux(surface=1),
    F.HydrogenFlux(surface=2),
]

derived_quantities = F.DerivedQuantities(
    list_of_derived_quantities,
    # filename="tds/derived_quantities.csv"  # optional set a filename to export the data to csv
)

model.exports = [derived_quantities]

model.initialise()
model.run()

t = derived_quantities.t
flux_left = derived_quantities.filter(fields="solute", surfaces=1).data
flux_right = derived_quantities.filter(fields="solute", surfaces=2).data

flux_total = -np.array(flux_left) - np.array(flux_right)

trap_1 = derived_quantities.filter(fields="1").data
trap_2 = derived_quantities.filter(fields="2").data
T = derived_quantities.filter(fields="T").data


indexes = np.where(np.array(t) > resting_time)
t = np.array(t)[indexes]
T = np.array(T)[indexes]
flux_total = np.array(flux_total)[indexes]
trap_1 = np.array(trap_1)[indexes]
trap_2 = np.array(trap_2)[indexes]

contribution_trap_1 = -np.diff(trap_1) / np.diff(t)
contribution_trap_2 = -np.diff(trap_2) / np.diff(t)

plt.plot(t, flux_total, linewidth=3)
plt.plot(t[1:], contribution_trap_1, linestyle="--", color="grey", alpha=0.5)
plt.fill_between(t[1:], 0, contribution_trap_1, facecolor="grey", alpha=0.1)
plt.plot(t[1:], contribution_trap_2, linestyle="--", color="grey", alpha=0.5)
plt.fill_between(t[1:], 0, contribution_trap_2, facecolor="grey", alpha=0.1)

exp_data = np.genfromtxt("ref_baldwin.csv", delimiter=",")
plt.scatter(exp_data[:, 0], exp_data[:, 1], alpha=0.6)

plt.xlim(left=resting_time)
plt.ylim(bottom=0)
plt.grid(alpha=0.3)
plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"Time (s)")
plt.gca().spines[["right", "top"]].set_visible(False)

for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"tds_baldwin.{ext}")
