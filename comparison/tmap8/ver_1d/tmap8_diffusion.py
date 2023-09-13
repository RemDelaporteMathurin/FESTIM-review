import festim as F
import numpy as np

my_model = F.Simulation()

vertices = np.concatenate(
    [
        np.linspace(0, 1, num=200),
    ]
)
my_model.mesh = F.MeshFromVertices(vertices)

my_model.materials = F.Material(id=1, D_0=1, E_D=0)

N = 3.1622e22
scale = 1e-4 * N
lambda_val = 3.16e-8
my_model.traps = F.Trap(
    k_0=1 / (lambda_val**2 * N),
    E_k=0,
    p_0=1e13,
    E_p=8.6e-3,
    materials=my_model.materials.materials[0],
    density=0.1 * N / scale,
)

my_model.T = F.Temperature(1000)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=1e-4 * N/ scale, field=0),
    F.DirichletBC(surfaces=2, value=0, field=0),
]

my_model.dt = F.Stepsize(initial_value=1e-2)
my_model.settings = F.Settings(
    absolute_tolerance=1e-10,
    relative_tolerance=1e-10,
    final_time=10,
)

derived_quantities = F.DerivedQuantities(
    [F.HydrogenFlux(surface=2)], filename="results/permeation_flux.csv"
)

xdmf_exports = [
    F.XDMFExport("solute", checkpoint=False),
    F.XDMFExport("1", checkpoint=False),
]

my_model.exports = [derived_quantities] #+ xdmf_exports
# my_model.log_level = 20
my_model.initialise()
my_model.run()
