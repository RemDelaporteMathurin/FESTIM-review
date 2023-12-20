import sympy as sp
import festim as F
import properties
import numpy as np

# IDs for volumes and surfaces (must be the same as in xdmf files)
id_lipb = 6
id_W = 9
id_structure = 7
id_baffle = 8
id_pipe_1_1 = 10
id_pipe_1_2 = 11
id_pipe_1_3 = 12
id_pipe_2_1 = 13
id_pipe_2_2 = 14
id_pipe_2_3 = 15
id_pipe_2_4 = 16
id_pipe_3_1 = 17
id_pipe_3_2 = 18
id_pipe_3_3 = 19
id_pipe_3_4 = 20
id_eurofers = [
    id_structure,
    id_baffle,
    id_pipe_1_1,
    id_pipe_1_2,
    id_pipe_1_3,
    id_pipe_2_1,
    id_pipe_2_2,
    id_pipe_2_3,
    id_pipe_2_4,
    id_pipe_3_1,
    id_pipe_3_2,
    id_pipe_3_3,
    id_pipe_3_4,
]

id_fw_coolant_interface_1 = 24
id_fw_coolant_interface_2 = 25
id_fw_coolant_interface_3 = 26
id_fw_coolant_interface_4 = 27
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
ids_fw_coolant_interface = [
    id_fw_coolant_interface_1,
    id_fw_coolant_interface_2,
    id_fw_coolant_interface_3,
    id_fw_coolant_interface_4,
]
ids_bz_coolant_interface = [
    id_bz_coolant_interface_1_1,
    id_bz_coolant_interface_1_2,
    id_bz_coolant_interface_1_3,
    id_bz_coolant_interface_2_1,
    id_bz_coolant_interface_2_2,
    id_bz_coolant_interface_2_3,
    id_bz_coolant_interface_2_4,
    id_bz_coolant_interface_3_1,
    id_bz_coolant_interface_3_2,
    id_bz_coolant_interface_3_3,
    id_bz_coolant_interface_3_4,
]

id_plasma_facing_surface = 23
id_inlet = 21
id_outlet = 22

my_heat_transfer_model = F.Simulation(log_level=20)

# define mesh
mesh_folder = "meshes/"
my_heat_transfer_model.mesh = F.MeshFromXDMF(
    volume_file=mesh_folder + "mesh_domains_3D.xdmf",
    boundary_file=mesh_folder + "mesh_boundaries_3D.xdmf",
)

# define materials
tungsten = F.Material(
    id=id_W,
    D_0=properties.D_0_W,
    E_D=properties.E_D_W,
    thermal_cond=properties.thermal_cond_W,
    heat_capacity=properties.Cp_W,
    rho=properties.rho_W,
)
materials_eurofers = [
    F.Material(
        id=id_vol,
        D_0=properties.D_0_eurofer,
        E_D=properties.E_D_eurofer,
        thermal_cond=properties.thermal_cond_eurofer,
        heat_capacity=properties.Cp_eurofer,
        rho=properties.rho_eurofer,
    )
    for id_vol in id_eurofers
]
lipb = F.Material(
    id=id_lipb,
    D_0=properties.D_0_lipb,
    E_D=properties.E_D_lipb,
    thermal_cond=properties.thermal_cond_lipb,
    heat_capacity=properties.Cp_lipb,
    rho=properties.rho_lipb,
)
my_heat_transfer_model.materials = F.Materials([tungsten, *materials_eurofers, lipb])

# define sources
my_heat_transfer_model.T = F.HeatTransferProblem(transient=False, linear_solver="mumps")
my_heat_transfer_model.sources = [
    F.Source(
        value=23.2e06 * sp.exp(-71.74 * F.x),
        volume=id_W,
        field="T",
    ),
    F.Source(
        value=sp.Piecewise(
            (9.6209e06 * sp.exp(-12.02 * F.x), F.x < 0.15),
            (4.7109e06 * sp.exp(-7.773 * F.x), F.x >= 0.15)
        ),
        volume=id_eurofers,
        field="T",
    ),
    F.Source(
        value=sp.Piecewise(
            (6.3034e05 * F.x ** (-0.789), F.x < 0.15),
            (3.4588e06 * sp.exp(-3.993 * F.x), F.x >= 0.15)
        ),
        volume=id_lipb,
        field="T",
    ),
]

# define boundary conditions
plasma_heat_flux = F.FluxBC(surfaces=id_plasma_facing_surface, value=0.5e06, field="T")
convective_flux_bz = F.ConvectiveFlux(
    h_coeff=5.025e03, T_ext=584.65, surfaces=ids_bz_coolant_interface
)
convective_flux_fw = F.ConvectiveFlux(
    h_coeff=8.876e03 * 5, T_ext=584.65, surfaces=ids_fw_coolant_interface
)
inlet_temp = F.DirichletBC(surfaces=id_inlet, value=598.15, field="T")
inlet_conc = F.DirichletBC(surfaces=id_inlet, value=0, field=0)
recomb_flux = F.RecombinationFlux(
    Kr_0=properties.Kr_0_eurofer,
    E_Kr=properties.E_Kr_eurofer,
    order=2,
    surfaces=[*ids_bz_coolant_interface, *ids_fw_coolant_interface],
)
implantation_flux = F.ImplantationDirichlet(
    surfaces=id_plasma_facing_surface,
    phi=1e20,
    R_p=3e-09,
    D_0=properties.D_0_W,
    E_D=properties.E_D_W,
)

my_heat_transfer_model.boundary_conditions = [
    plasma_heat_flux,
    convective_flux_bz,
    convective_flux_fw,
    inlet_temp,
    inlet_conc,
    recomb_flux,
    implantation_flux,
]

# define solving parameters
my_heat_transfer_model.settings = F.Settings(
    transient=False,
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    linear_solver="mumps",
)

