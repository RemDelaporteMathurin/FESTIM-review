import festim as F
import numpy as np
import sympy as sp


class PointValue(F.DerivedQuantity):
    def __init__(self, field, x) -> None:
        super().__init__(field)
        self.x = x
        self.title = f"{field} value {x:.2e}"

    def compute(self):
        return self.function(self.x)


my_model = F.Simulation()

my_model.mesh = F.MeshFromVertices(np.linspace(0, 100, num=1000))

my_model.initial_conditions = [
    F.InitialCondition(field="solute", value=sp.Piecewise((1, F.x < 10), (0, True)))
]

my_model.materials = F.Material(id=1, D_0=1, E_D=0)

my_model.T = F.Temperature(300)

derived_quantities = F.DerivedQuantities(
    [
        PointValue("solute", x=0),
        PointValue("solute", x=10),
        PointValue("solute", x=12),
    ],
    filename="results/derived_quantities.csv",
)

my_model.exports = [derived_quantities]

my_model.dt = F.Stepsize(0.05)

my_model.settings = F.Settings(
    absolute_tolerance=1e-10, relative_tolerance=1e-10, final_time=100
)

my_model.initialise()
my_model.run()
