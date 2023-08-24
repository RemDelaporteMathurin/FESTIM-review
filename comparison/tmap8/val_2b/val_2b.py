import festim as F
import fenics as f
import numpy as np
import sympy as sp


D_0_beo_charging = 1.40e-4
E_D_beo_charging = 24408 * F.k_B

D_0_beo_desorption = 7e-5
E_D_beo_desorption = 27000 * F.k_B

beo = F.Material(
    id=1,
    name="beo",
    D_0=D_0_beo_charging,
    E_D=E_D_beo_charging,
    borders=[0, 18e-9],
    S_0=5.00e20,
    E_S=-9377.7 * F.k_B,
)
be = F.Material(
    id=2,
    name="be",
    D_0=8.0e-9,
    E_D=4220 * F.k_B,
    borders=[18e-9, 0.4e-3 / 2],
    S_0=7.156e27,
    E_S=11606 * F.k_B,
)

model_charging = F.Simulation()

model_charging.materials = [beo, be]

vertices = np.concatenate(
    [
        np.arange(*beo.borders, step=0.5e-9),
        [beo.borders[-1]],
        np.arange(*be.borders, step=0.5e-5),
        [be.borders[-1]]
    ]
)

model_charging.mesh = F.MeshFromVertices(vertices)

time_charging = 180000
time_cool_down = 2400
time_start_tds = time_charging + time_cool_down
temperature_ramp = 0.05
tds_duration = (1073 - 300)/(temperature_ramp)


enclosure_pressure = sp.Piecewise(
    (13300.0, F.t < time_charging + 15),  # + 15 is from tmap8's case.
    (1e-6, F.t < time_start_tds),
    (1e-3, True),
)
model_charging.boundary_conditions = [
    F.SievertsBC(surfaces=1, S_0=beo.S_0, E_S=beo.E_S, pressure=enclosure_pressure)
]

loading_temperature = 773
cooling_time_constant = 45 * 60
model_charging.T = F.Temperature(
    sp.Piecewise(
        (loading_temperature, F.t < time_charging),
        (
            loading_temperature - ((1 - sp.exp(-(F.t - time_charging) / cooling_time_constant)) * 475),
            F.t <= time_start_tds,
        ),
        (300 + temperature_ramp * (F.t - time_start_tds), True),
    )
)

model_charging.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    final_time=time_start_tds,
    chemical_pot=True,
)

model_charging.dt = F.Stepsize(initial_value=10, stepsize_change_ratio=1.1, t_stop=time_charging, stepsize_stop_max=60)

derived_quantities = F.DerivedQuantities(
    [
        F.AverageVolume("T", volume=1),
        F.AverageVolume("T", volume=2),
    ],
    filename="results/derived_quantities_loading.csv"
)

model_charging.exports = [
    F.XDMFExport("solute", checkpoint=False),
    F.XDMFExport("solute", filename="mobile_concentration_checkpoint.xdmf", checkpoint=True),
    F.XDMFExport("T", checkpoint=False),
    F.TXTExport(field="solute", label="solute", folder="results", times=[time_charging]),
    derived_quantities
]

# model_charging.log_level = 20
model_charging.initialise()
model_charging.run()



model_desorb = F.Simulation()
beo.D_0 = D_0_beo_desorption
beo.E_D = E_D_beo_desorption

model_desorb.materials = model_charging.materials

model_desorb.mesh = model_charging.mesh

model_desorb.boundary_conditions = model_charging.boundary_conditions

model_desorb.settings = model_charging.settings
model_desorb.settings.final_time = time_start_tds + tds_duration

model_desorb.dt = model_charging.dt
model_desorb.stepsize_stop_max = 10

model_desorb.T = model_charging.T

model_desorb.initial_conditions = [F.InitialCondition(field=0, value="mobile_concentration_checkpoint.xdmf", label="mobile_concentration", time_step=-1)]

derived_quantities = F.DerivedQuantities(
    [
        F.HydrogenFlux(surface=1),
        F.AverageVolume("T", volume=1),
        F.AverageVolume("T", volume=2),
    ],
    filename="results/derived_quantities.csv"
)

model_desorb.exports = [
    F.XDMFExport("solute", checkpoint=False, filename="mobile_concentration_desorb.xdmf"),
    F.XDMFExport("T", checkpoint=False, filename="temperature_desorb.xdmf"),
    derived_quantities
]
# model_desorb.log_level = 20
model_desorb.initialise()
model_desorb.t = time_start_tds
# print(type(model_desorb.h_transport_problem.mobile))
# mobile_conc_charging = model_charging.h_transport_problem.mobile.solution

# model_desorb.h_transport_problem.mobile.previous_solution.assign(mobile_conc_charging)
model_desorb.run()
