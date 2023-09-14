import festim as F
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

model = F.Simulation()


vertices = np.concatenate(
    [
        np.linspace(0, 30e-9, num=200),
        np.linspace(30e-9, 3e-6, num=300),
        np.linspace(3e-6, 20e-6, num=200),
    ]
)

model.mesh = F.MeshFromVertices(vertices)

tungsten = F.Material(
    id=1,
    D_0=4.1e-07,  # m2/s
    E_D=0.39,  # eV
)

model.materials = tungsten


implantation_time = 400  # s

ion_flux = sp.Piecewise((2.5e19, F.t <= implantation_time), (0, True))

source_term = F.ImplantationFlux(
    flux=ion_flux, imp_depth=4.5e-9, width=2.5e-9, volume=1  # H/m2/s  # m  # m
)

model.sources = [source_term]

w_atom_density = 6.3e28  # atom/m3

trap_1 = F.Trap(
    k_0=4.1e-7 / (1.1e-10**2 * 6 * w_atom_density),
    E_k=0.39,
    p_0=1e13,
    E_p=0.87,
    density=1.3e-3 * w_atom_density,
    materials=tungsten,
)
trap_2 = F.Trap(
    k_0=4.1e-7 / (1.1e-10**2 * 6 * w_atom_density),
    E_k=0.39,
    p_0=1e13,
    E_p=1.0,
    density=4e-4 * w_atom_density,
    materials=tungsten,
)

center = 4.5e-9
width = 2.5e-9
distribution = (
    1 / (width * (2 * sp.pi) ** 0.5) * sp.exp(-0.5 * ((F.x - center) / width) ** 2)
)
trap_3 = F.ExtrinsicTrap(
    k_0=4.1e-7 / (1.1e-10**2 * 6 * w_atom_density),
    E_k=0.39,
    p_0=1e13,
    E_p=1.5,
    phi_0=ion_flux,
    n_amax=1e-01 * w_atom_density,
    f_a=distribution,
    eta_a=6e-4,
    n_bmax=1e-02 * w_atom_density,
    f_b=sp.Piecewise((1e6, F.x < 1e-6), (0, True)),
    eta_b=2e-4,
    materials=tungsten,
)

model.traps = [trap_1, trap_2, trap_3]

model.boundary_conditions = [F.DirichletBC(surfaces=[1, 2], value=0, field=0)]

implantation_temp = 300  # K
temperature_ramp = 8  # K/s

start_tds = implantation_time + 50  # s

model.T = F.Temperature(
    value=sp.Piecewise(
        (implantation_temp, F.t < start_tds),
        (implantation_temp + temperature_ramp * (F.t - start_tds), True),
    )
)

model.dt = F.Stepsize(
    initial_value=0.5,
    stepsize_change_ratio=1.1,
    t_stop=implantation_time - 20,
    stepsize_stop_max=0.5,
    dt_min=1e-05,
)

model.settings = F.Settings(
    absolute_tolerance=1e10, relative_tolerance=1e-09, final_time=500
)

list_of_derived_quantities = [
    F.TotalVolume("solute", volume=1),
    F.TotalVolume("retention", volume=1),
    F.TotalVolume("1", volume=1),
    F.TotalVolume("2", volume=1),
    F.TotalVolume("3", volume=1),
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
trap_3 = derived_quantities.filter(fields="3").data
T = derived_quantities.filter(fields="T").data


indexes = np.where(np.array(t) > start_tds)
t = np.array(t)[indexes]
T = np.array(T)[indexes]
flux_total = np.array(flux_total)[indexes]
trap_1 = np.array(trap_1)[indexes]
trap_2 = np.array(trap_2)[indexes]
trap_3 = np.array(trap_3)[indexes]

contribution_trap_1 = -np.diff(trap_1) / np.diff(t)
contribution_trap_2 = -np.diff(trap_2) / np.diff(t)
contribution_trap_3 = -np.diff(trap_3) / np.diff(t)

plt.plot(T, flux_total, linewidth=3, label='FESTIM')
plt.plot(T[1:], contribution_trap_1, linestyle="--", color="grey", alpha=0.5)
plt.fill_between(T[1:], 0, contribution_trap_1, facecolor="grey", alpha=0.1)
plt.plot(T[1:], contribution_trap_2, linestyle="--", color="grey", alpha=0.5)
plt.fill_between(T[1:], 0, contribution_trap_2, facecolor="grey", alpha=0.1)
plt.plot(T[1:], contribution_trap_3, linestyle="--", color="grey", alpha=0.5)
plt.fill_between(T[1:], 0, contribution_trap_3, facecolor="grey", alpha=0.1)

exp_data = np.genfromtxt("ref_ogorodnikova.csv", delimiter=",")
plt.scatter(exp_data[:, 0], exp_data[:, 1], alpha=0.6, label='experiment')

plt.xlim(300, 700)
plt.ylim(bottom=-1.25e18, top=0.6e19)
plt.grid(alpha=0.3)
plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"Temperature (K)")
plt.gca().spines[["right", "top"]].set_visible(False)
plt.legend()
for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"tds_ogorodnikova.{ext}")
