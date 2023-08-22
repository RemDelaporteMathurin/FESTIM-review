import festim as F
import numpy as np

my_model = F.Simulation()

my_model.mesh = F.MeshFromVertices(np.linspace(0, 1, num=20))

my_model.materials = F.Material(id=1, D_0=1, E_D=0)

alpha_t = 1e15
N = 3.1622e22
cl = N * 1e-4
ct0 = 0.1
my_model.traps = F.Trap(k_0=alpha_t/(N/cl), E_k=0, p_0=1e13, E_p=8, materials=my_model.materials.materials[0], density=ct0 * N/cl)

my_model.T = F.Temperature(1000)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=1, field=0),
    F.DirichletBC(surfaces=2, value=0, field=0)
]

my_model.dt = F.Stepsize(1)
my_model.settings = F.Settings(
    absolute_tolerance=1e-1,
    relative_tolerance=1e-10,
    final_time=1000,
    traps_element_type="DG"
)

derived_quantities = F.DerivedQuantities(
    [F.HydrogenFlux(surface=2)],
    filename="results/permeation_flux.csv"
)
my_model.exports = [derived_quantities]
my_model.log_level = 20
my_model.initialise()
my_model.run()
