import festim as F
import numpy as np
import fenics as f

encl_vol = 5.20e-11  # m3  same
encl_surf = 2.16e-6  # m2  same
l = 3.3e-5  # m same
R = 8.314  # same
avogadro = 6.022e23  # mol-1  same
temperature = 2373  # K  same
initial_pressure = 1e6  # Pa  same
solubility = 7.244e22 / temperature  # H/m3/Pa  # same
diffusivity = 2.6237e-11  # m2/s  almost same


def henrys_law(T, S_0, E_S, pressure):
    S = S_0 * f.exp(-E_S / F.k_B / T)
    return S * pressure


class PressureExport(F.DerivedQuantity):
    def __init__(self, **kwargs):
        super().__init__(field="solute", **kwargs)
        self.title = "enclosure_pressure"
        self.data = []

    def compute(self):
        return float(left_bc.pressure)


class CustomHenrysBC(F.HenrysBC):
    def create_expression(self, T):
        value_BC = F.BoundaryConditionExpression(
            T,
            henrys_law,
            S_0=self.H_0,
            E_S=self.E_H,
            pressure=self.pressure,
        )
        self.expression = value_BC
        self.sub_expressions = [self.pressure]


class CustomSimulation(F.Simulation):
    def iterate(self):
        super().iterate()
        # Update pressure based on flux
        left_flux_val = left_flux.compute()
        old_pressure = float(left_bc.pressure)
        new_pressure = (
            old_pressure
            - (left_flux_val * encl_surf / encl_vol * R * self.T.T(0) / avogadro)
            * self.dt.value
        )
        left_bc.pressure.assign(new_pressure)


my_model = CustomSimulation()

vertices = np.linspace(0, l, 100)

my_model.mesh = F.MeshFromVertices(vertices)

my_model.materials = F.Material(
    id=1,
    D_0=diffusivity,
    E_D=0,
)

left_bc = CustomHenrysBC(
    surfaces=1, H_0=solubility, E_H=0, pressure=f.Constant(initial_pressure)
)

my_model.boundary_conditions = [
    left_bc,
    F.DirichletBC(surfaces=2, value=0, field="solute"),
]

my_model.T = F.Temperature(temperature)

my_model.settings = F.Settings(
    absolute_tolerance=1e8,
    relative_tolerance=1e-10,
    final_time=140,
)

left_flux = F.HydrogenFlux(surface=1)
right_flux = F.HydrogenFlux(surface=2)
pressure_export = PressureExport()
derived_quantities = F.DerivedQuantities([left_flux, right_flux, pressure_export])

my_model.exports = [
    # F.XDMFExport("solute", filename="enclosure/mobile.xdmf", checkpoint=False),
    derived_quantities,
]

my_model.dt = F.Stepsize(initial_value=0.1)

# my_model.log_level = 10

my_model.initialise()
my_model.run()
print(f"final pressure is {float(left_bc.pressure)}")
