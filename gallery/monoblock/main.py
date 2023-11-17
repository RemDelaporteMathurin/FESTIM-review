import festim as F
import numpy as np

my_model = F.Simulation()

id_W = 6  # volume W
id_Cu = 7  # volume Cu
id_CuCrZr = 8  # volume CuCrZr
id_W_top = 9
id_coolant = 10
id_poloidal_gap_W = 11
id_poloidal_gap_Cu = 12
id_toroidal_gap = 13
id_bottom = 14
id_top_pipe = 15


# ----------------------------- Mesh ----------------------------- #

my_model.mesh = F.MeshFromXDMF(
    volume_file="mesh/mesh_cells.xdmf",
    boundary_file="mesh/mesh_facets.xdmf",
)

# ----------------------------- Materials ----------------------------- #


def polynomial(coeffs, x, main):
    val = coeffs[0]
    for i in range(1, 4):
        if main:
            val += coeffs[i] * np.float_power(x, i)
        else:
            val += coeffs[i] * x**i
    return val


def thermal_cond_W(T, main=False):
    coeffs = [1.75214e2, -1.07335e-1, 5.03006e-5, -7.84154e-9]
    return polynomial(coeffs, T, main=main)


def thermal_cond_Cu(T, main=False):
    coeffs = [4.02301e02, -7.88669e-02, 3.76147e-05, -3.93153e-08]
    return polynomial(coeffs, T, main=main)


def thermal_cond_CuCrZr(T, main=False):
    coeffs = [3.12969e2, 2.57678e-01, -6.45110e-4, 5.25780e-7]
    return polynomial(coeffs, T, main=main)


atom_density_W = 6.3222e28  # atomic density m^-3
atom_density_Cu = 8.4912e28  # atomic density m^-3
atom_density_CuCrZr = 2.6096e28  # atomic density m^-3

tungsten = F.Material(
    id=id_W,
    D_0=4.10e-7,
    E_D=0.390,
    S_0=1.870e24,
    E_S=1.04,
    thermal_cond=thermal_cond_W,
)

copper = F.Material(
    id=id_Cu,
    D_0=6.60e-7,
    E_D=0.387,
    S_0=3.14e24,
    E_S=0.572,
    thermal_cond=thermal_cond_Cu,
)

cucrzr = F.Material(
    id=id_CuCrZr,
    D_0=3.92e-7,
    E_D=0.418,
    S_0=4.28e23,
    E_S=0.387,
    thermal_cond=thermal_cond_CuCrZr,
)

my_model.materials = F.Materials([tungsten, copper, cucrzr])


# ----------------------------- Traps ----------------------------- #

my_model.traps = F.Traps(
    [
        F.Trap(
            k_0=8.96e-17,
            E_k=tungsten.E_D,
            p_0=1e13,
            E_p=0.87,
            density=1.3e-3 * atom_density_W,
            materials=tungsten,
        ),
        F.Trap(
            k_0=[8.96e-17, 6e-17, 1.2e-16],
            E_k=[tungsten.E_D, copper.E_D, cucrzr.E_D],
            p_0=[1e13, 8e13, 8e13],
            E_p=[1.0, 0.5, 0.85],
            density=[
                4e-4 * atom_density_W,
                5e-5 * atom_density_Cu,
                5e-5 * atom_density_CuCrZr,
            ],
            materials=[tungsten, copper, cucrzr],
        ),
    ]
)

# ----------------------------- Temperature ----------------------------- #

my_model.T = F.HeatTransferProblem(transient=False)


# ------------------------- Boundary conditions ------------------------- #

heat_flux_top = F.FluxBC(surfaces=id_W_top, value=10e6, field="T")
convective_heat_flux_coolant = F.ConvectiveFlux(
    h_coeff=7e04, T_ext=323, surfaces=id_coolant
)

heat_transfer_bcs = [heat_flux_top, convective_heat_flux_coolant]

instantaneous_recombination_poloidal_W = F.DirichletBC(
    value=0, surfaces=id_poloidal_gap_W, field="solute"
)
instantaneous_recombination_poloidal_Cu = F.DirichletBC(
    value=0, surfaces=id_poloidal_gap_Cu, field="solute"
)
instantaneous_recombination_toroidal = F.DirichletBC(
    value=0, surfaces=id_toroidal_gap, field="solute"
)
instantaneous_recombination_bottom = F.DirichletBC(
    value=0, surfaces=id_bottom, field="solute"
)
instantaneous_recombination_top_pipe = F.DirichletBC(
    value=0, surfaces=id_top_pipe, field="solute"
)
instantaneous_recombination_coolant = F.DirichletBC(
    value=0, surfaces=id_coolant, field="solute"
)

# recombination_poloidal_W = F.RecombinationFlux(
#     Kr_0=3.2e-15, E_Kr=1.16, order=2, surfaces=id_poloidal_gap_W
# )

# recombination_poloidal_Cu = F.RecombinationFlux(
#     Kr_0=2.9e-14, E_Kr=1.92, order=2, surfaces=id_poloidal_gap_W
# )

# recombination_toroidal = F.RecombinationFlux(
#     Kr_0=3.2e-15, E_Kr=1.16, order=2, surfaces=id_toroidal_gap
# )

# recombination_flux_coolant = F.RecombinationFlux(
#     Kr_0=2.9e-14, E_Kr=1.92, order=2, surfaces=id_coolant
# )

# recombination_top_pipe = F.RecombinationFlux(
#     Kr_0=2.9e-14, E_Kr=1.92, order=2, surfaces=id_top_pipe
# )

h_implantation_top = F.ImplantationDirichlet(
    surfaces=id_W_top, phi=1.60e22, R_p=1e-9, D_0=tungsten.D_0, E_D=tungsten.E_D
)

h_transport_bcs = [
    h_implantation_top,
    instantaneous_recombination_poloidal_W,
    instantaneous_recombination_poloidal_Cu,
    instantaneous_recombination_toroidal,
    instantaneous_recombination_bottom,
    instantaneous_recombination_top_pipe,
    instantaneous_recombination_coolant,
]


my_model.boundary_conditions = heat_transfer_bcs + h_transport_bcs

# ------------------------- Settings ------------------------- #


my_model.settings = F.Settings(
    absolute_tolerance=1e4,
    relative_tolerance=1e-5,
    maximum_iterations=15,
    traps_element_type="DG",
    chemical_pot=True,
    transient=True,
    final_time=1e6,
    linear_solver="mumps",
)

my_model.dt = F.Stepsize(
    initial_value=1e5, stepsize_change_ratio=1.1
)  # replacing initial_value by 1e6 produces very similar results

# ------------------------- Exports ------------------------- #

derived_quantities = F.DerivedQuantities(
    [
        F.TotalVolume(field="solute", volume=id_W),
        F.TotalVolume(field="solute", volume=id_Cu),
        F.TotalVolume(field="solute", volume=id_CuCrZr),
        F.TotalVolume(field="retention", volume=id_W),
        F.TotalVolume(field="retention", volume=id_Cu),
        F.TotalVolume(field="retention", volume=id_CuCrZr),
        F.TotalVolume(field="1", volume=id_W),
        F.TotalVolume(field="2", volume=id_W),
        F.TotalVolume(field="2", volume=id_Cu),
        F.TotalVolume(field="2", volume=id_CuCrZr),
        F.SurfaceFlux(field="solute", surface=id_W_top),
        F.SurfaceFlux(field="solute", surface=id_coolant),
        F.SurfaceFlux(field="solute", surface=id_poloidal_gap_W),
        F.SurfaceFlux(field="solute", surface=id_poloidal_gap_Cu),
        F.SurfaceFlux(field="solute", surface=id_toroidal_gap),
        F.SurfaceFlux(field="solute", surface=id_top_pipe),
        F.SurfaceFlux(field="solute", surface=id_bottom),
    ],
    filename="./derived_quantities.csv",
)

my_model.exports = F.Exports(
    [
        derived_quantities,
        F.XDMFExport("T"),
        F.XDMFExport("solute", checkpoint=True),
        F.XDMFExport("retention", checkpoint=True),
        F.XDMFExport("1", checkpoint=True),
        F.XDMFExport("2", checkpoint=True),
    ]
)

my_model.log_level = 20

if __name__ == "__main__":
    my_model.initialise()
    my_model.run()
