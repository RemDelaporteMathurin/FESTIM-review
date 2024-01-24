"""
Needs to be run in serial
"""
import fenics as fe
import festim as F
import properties


# IDs for volumes and surfaces (must be the same as in xdmf files)
id_lipb = 6
id_inlet = 21
id_outlet = 22

mesh_folder = "meshes/"

# ##### Create SubMesh ##### #
mesh_full = F.MeshFromXDMF(
    volume_file="meshes/mesh_domains_2D.xdmf",
    boundary_file=mesh_folder + "mesh_boundaries_2D.xdmf",
)

mesh_sub = fe.SubMesh(
    mesh_full.mesh, mesh_full.volume_markers, id_lipb
)  # doesn't work in parrallel

volume_markers_sub = fe.MeshFunction("size_t", mesh_sub, mesh_sub.topology().dim(), 1)
surface_markers_sub = fe.MeshFunction("size_t", mesh_sub, 1, 0)

# ##### Define Function Spaces ##### #

V_ele = fe.VectorElement("CG", mesh_sub.ufl_cell(), 2)
Q_ele = fe.FiniteElement("CG", mesh_sub.ufl_cell(), 1)
W = fe.FunctionSpace(mesh_sub, fe.MixedElement([V_ele, Q_ele]))

# ##### Boundary conditions ##### #

boundary = fe.CompiledSubDomain("on_boundary")
boundary_inlet = fe.CompiledSubDomain(
    "on_boundary && near(x[0], L, tol) && x[1] <= h", tol=1e-14, L=0.567, h=0.066
)
boundary_oulet = fe.CompiledSubDomain(
    "on_boundary && near(x[0], L, tol) && x[1] > h + DOLFIN_EPS",
    tol=1e-14,
    L=0.567,
    h=0.066,
)

id_walls = 5
boundary.mark(surface_markers_sub, id_walls)
boundary_inlet.mark(surface_markers_sub, id_inlet)
boundary_oulet.mark(surface_markers_sub, id_outlet)

inlet_temperature = 598.15  # units: K
inlet_velocity = 2e-04  # units: ms-1
outlet_pressure = 0  # units: Pa

# Simulation boundary conditions
non_slip = fe.Constant((0.0, 0.0, 0.0))
inflow = fe.DirichletBC(
    W.sub(0), fe.Constant((-inlet_velocity, 0.0, 0.0)), surface_markers_sub, id_inlet
)
walls = fe.DirichletBC(W.sub(0), non_slip, surface_markers_sub, id_walls)
pressure_outlet = fe.DirichletBC(W.sub(1), fe.Constant(0), surface_markers_sub, id_outlet)
bcs = [inflow, pressure_outlet, walls]

g = fe.Constant((0.0, -9.81, 0.0))
T_0 = inlet_temperature

# ##### CFD --> Define Variational Parameters ##### #

v, q = fe.TestFunctions(W)
up = fe.Function(W)
u, p = fe.split(up)

# ##### CFD --> Fluid Materials properties ##### #

V_CG1 = fe.FunctionSpace(mesh_sub, "CG", 1)
print("Projecting temperature field onto mesh")
mesh_temperature = mesh_full.mesh
V_CG1 = fe.FunctionSpace(mesh_temperature, "CG", 1)
V_CG1_sub = fe.FunctionSpace(mesh_sub, "CG", 1)
temperature_field = fe.Function(V_CG1)

fe.XDMFFile("Results/temperature_field_slice.xdmf").read_checkpoint(temperature_field, "T", -1)
T = fe.project(temperature_field, V_CG1_sub, solver_type="mumps")

# Fluid properties
rho_0 = properties.rho_0_lipb
mu = properties.visc_lipb(T)
beta = properties.beta_lipb(T)

# ##### Solver ##### #
dx = fe.Measure("dx", subdomain_data=volume_markers_sub)
ds = fe.Measure("ds", subdomain_data=surface_markers_sub)

F = (
    #           momentum
    rho_0 * fe.inner(fe.grad(u), fe.grad(v)) * dx
    - fe.inner(p, fe.div(v)) * dx
    + mu * fe.inner(fe.dot(fe.grad(u), u), v) * dx
    + (beta * rho_0) * fe.inner((T - T_0) * g, v) * dx
    #           continuity
    + fe.inner(fe.div(u), q) * dx
)
print("Solving Navier-Stokes")
fe.solve(F == 0, up, bcs, solver_parameters={"newton_solver": {"linear_solver": "mumps"}})

u_sub, p_sub = up.split()

# ##### extend from subdomain to full mesh ##### #

print("Extending the function")

ele_full = fe.VectorElement("CG", mesh_full.mesh.ufl_cell(), 2)
V = fe.FunctionSpace(mesh_full.mesh, ele_full)
u_full = fe.Function(V)
v_full = fe.TestFunction(V)

mesh_full.define_markers()
mesh_full.define_measures()

F = fe.inner(u_full, v_full) * mesh_full.dx
F += -fe.inner(u_sub, v_full) * mesh_full.dx(id_lipb)
print("Projecting onto full mesh")
fe.solve(
    F == 0,
    u_full,
    bcs=[],
    solver_parameters={"newton_solver": {"linear_solver": "mumps"}},
)

fe.XDMFFile("Results/velocity_field.xdmf").write_checkpoint(
    u_full, "u", 0, fe.XDMFFile.Encoding.HDF5, append=False
)
