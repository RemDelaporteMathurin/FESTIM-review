import festim as F
import numpy as np

my_model = F.Simulation()

vertices = np.concatenate(
    [
        np.linspace(0, 1e-6, num=10000),
        np.linspace(1e-6, 1e-4, num=10000),
    ]
)
my_model.mesh = F.MeshFromVertices(vertices)

my_model.materials = F.Material(id=1, D_0=1e-2, E_D=0)

alpha_t = 1e15
N = 3.1622e22
ct0 = 0.1
my_model.traps = F.Trap(
    k_0=alpha_t / N,
    E_k=0,
    p_0=1e13,
    E_p=8,
    materials=my_model.materials.materials[0],
    density=ct0 * N,
)

my_model.T = F.Temperature(1000)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=1e-4 * N, field=0),
    F.DirichletBC(surfaces=2, value=0, field=0),
]

my_model.dt = F.Stepsize(initial_value=1e-6, stepsize_change_ratio=1.1)
my_model.settings = F.Settings(
    absolute_tolerance=1e8,
    relative_tolerance=1e-6,
    final_time=1000,
    traps_element_type="DG",
)

derived_quantities = F.DerivedQuantities(
    [F.HydrogenFlux(surface=2)], filename="results/permeation_flux.csv"
)

xdmf_exports = [
    F.XDMFExport("solute", checkpoint=False),
    F.XDMFExport("1", checkpoint=False),
]

my_model.exports = [derived_quantities] + xdmf_exports
my_model.log_level = 20
my_model.initialise()
my_model.run()
