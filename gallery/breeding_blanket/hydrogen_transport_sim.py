import festim as F
import sympy as sp
import properties
import fenics as fe

# IDs for volumes and surfaces (must be the same as in xdmf files)

id_lipb = 6
id_structure = 7
id_baffle = 8
id_W = 9
id_bz_pipe_1_1 = 10
id_bz_pipe_1_2 = 11
id_bz_pipe_1_3 = 12
id_bz_pipe_2_1 = 13
id_bz_pipe_2_2 = 14
id_bz_pipe_2_3 = 15
id_bz_pipe_2_4 = 16
id_bz_pipe_3_1 = 17
id_bz_pipe_3_2 = 18
id_bz_pipe_3_3 = 19
id_bz_pipe_3_4 = 20
id_eurofers = [
    id_structure,
    id_baffle,
    id_bz_pipe_1_1,
    id_bz_pipe_1_2,
    id_bz_pipe_1_3,
    id_bz_pipe_2_1,
    id_bz_pipe_2_2,
    id_bz_pipe_2_3,
    id_bz_pipe_2_4,
    id_bz_pipe_3_1,
    id_bz_pipe_3_2,
    id_bz_pipe_3_3,
    id_bz_pipe_3_4,
]

id_inlet = 21
id_outlet = 22
id_plasma_facing_wall = 23

id_fw_coolant_interface_1_4 = 24
id_fw_coolant_interface_1_3 = 25
id_fw_coolant_interface_1_2 = 26
id_fw_coolant_interface_1_1 = 27
ids_fw_coolant_interfaces = [
    id_fw_coolant_interface_1_1,
    id_fw_coolant_interface_1_2,
    id_fw_coolant_interface_1_3,
    id_fw_coolant_interface_1_4,
]

id_bz_coolant_interface_1_1 = 28
id_bz_coolant_interface_1_2 = 29
id_bz_coolant_interface_1_3 = 30
id_bz_coolant_interface_2_1 = 31
id_bz_coolant_interface_2_2 = 32
id_bz_coolant_interface_2_3 = 33
id_bz_coolant_interface_2_4 = 34
id_bz_coolant_interface_3_1 = 35
id_bz_coolant_interface_3_2 = 36
id_bz_coolant_interface_3_3 = 37
id_bz_coolant_interface_3_4 = 38
ids_bz_coolant_interfaces = [
    id_bz_coolant_interface_1_3,
    id_bz_coolant_interface_1_2,
    id_bz_coolant_interface_1_1,
    id_bz_coolant_interface_2_1,
    id_bz_coolant_interface_2_2,
    id_bz_coolant_interface_2_3,
    id_bz_coolant_interface_2_4,
    id_bz_coolant_interface_3_1,
    id_bz_coolant_interface_3_2,
    id_bz_coolant_interface_3_3,
    id_bz_coolant_interface_3_4,
]

my_model = F.Simulation(log_level=20)

# define mesh
mesh_folder = "meshes/"
my_model.mesh = F.MeshFromXDMF(
    volume_file=mesh_folder + "mesh_domains_2D.xdmf",
    boundary_file=mesh_folder + "mesh_boundaries_2D.xdmf",
)

# define materials
tungsten = F.Material(
    id=id_W,
    D_0=properties.D_0_W,
    E_D=properties.E_D_W,
    S_0=properties.S_0_W,
    E_S=properties.E_S_W,
)
materials_eurofers = [
    F.Material(
        id=id_vol,
        D_0=properties.D_0_eurofer,
        E_D=properties.E_D_eurofer,
        S_0=properties.S_0_eurofer,
        E_S=properties.E_S_eurofer,
    )
    for id_vol in id_eurofers
]
lipb = F.Material(
    id=id_lipb,
    D_0=properties.D_0_lipb,
    E_D=properties.E_D_lipb,
    S_0=properties.S_0_lipb,
    E_S=properties.E_S_lipb,
)
my_model.materials = F.Materials([tungsten, *materials_eurofers, lipb])

# define traps
trap_W_1 = F.Trap(
    k_0=properties.D_0_W / (1.1e-10**2 * 6 * properties.atom_density_W),
    E_k=properties.E_D_W,
    p_0=1e13,
    E_p=0.87,
    density=1.3e-3 * properties.atom_density_W,
    materials=tungsten,
)
trap_W_2 = F.Trap(
    k_0=properties.D_0_W / (1.1e-10**2 * 6 * properties.atom_density_W),
    E_k=properties.E_D_W,
    p_0=1e13,
    E_p=1.00,
    density=4e-4 * properties.atom_density_W,
    materials=tungsten,
)
trap_eurofer_1 = F.Trap(
    k_0=properties.D_0_eurofer
    / (1.1e-10**2)
    * 0.8165
    / properties.atom_density_eurofer,
    E_k=properties.E_D_eurofer,
    p_0=1e13,
    E_p=properties.trap_energy_eurofer,
    density=properties.trap_density_eurofer,
    materials=materials_eurofers,
)
my_model.traps = F.Traps(
    [
        trap_W_1,
        trap_W_2,
        trap_eurofer_1,
    ]
)

# define sources
my_model.sources = [
    F.Source(
        value=6.022e23
        * 1e6
        * (
            1.044e-11 * sp.exp(-0.2182 * F.x * 1e2)
            + 6.514e-12 * sp.exp(-0.04106 * F.x * 1e2)
        ),
        volume=id_lipb,
        field="solute",
    ),
]

# define temperature
temperature_field = "Results/temperature_field_slice.xdmf"
my_model.T = F.TemperatureFromXDMF(filename=temperature_field, label="T")

# define boundary conditions
inlet_h_concentration = F.DirichletBC(surfaces=id_inlet, value=0, field=0)
coolant_boundary_recombination_flux = F.RecombinationFlux(
    Kr_0=properties.Kr_0_eurofer,
    E_Kr=properties.E_Kr_eurofer,
    order=2,
    surfaces=[*ids_bz_coolant_interfaces, *ids_fw_coolant_interfaces],
)
first_wall_implantation_flux = F.ImplantationDirichlet(
    surfaces=id_plasma_facing_wall,
    phi=1e20,
    R_p=3e-09,
    D_0=properties.D_0_W,
    E_D=properties.E_D_W,
)

my_model.boundary_conditions = [
    inlet_h_concentration,
    coolant_boundary_recombination_flux,
    first_wall_implantation_flux,
]

# define exports
folder_results = "Results/"
my_model.exports = F.Exports(
    [
        F.XDMFExport("solute", folder=folder_results, mode=1),
    ]
)

# transient parameters
my_model.dt = F.Stepsize(initial_value=1000, stepsize_change_ratio=1.05)


# define solving parameters
my_model.settings = F.Settings(
    transient=True,
    final_time=2000,
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    maximum_iterations=50,
    chemical_pot=True,
    linear_solver="mumps",
)

my_model.initialise()

V_ele = fe.VectorElement("CG", my_model.mesh.mesh.ufl_cell(), 2)
V_u = fe.FunctionSpace(my_model.mesh.mesh, V_ele)

velocity_field = "Results/velocity_field.xdmf"
u = fe.Function(V_u, name="velocity")
fe.XDMFFile(velocity_field).read_checkpoint(u, "u", -1)

# modify the form F
id_flow = id_lipb
test_function_solute = my_model.h_transport_problem.mobile.test_function
solute = my_model.h_transport_problem.mobile.solution
dx = my_model.mesh.dx
S_lipb = properties.S_0_lipb * fe.exp(-properties.E_S_lipb / F.k_B / my_model.T.T)
my_model.h_transport_problem.F += fe.inner(
    fe.dot(fe.grad(S_lipb * solute), u), test_function_solute
) * dx(id_flow)

# run the simulation with the modified formulation
my_model.run()
