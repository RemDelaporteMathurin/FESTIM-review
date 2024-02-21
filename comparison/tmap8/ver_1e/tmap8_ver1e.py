import festim as F
import numpy as np


class PointValue(F.DerivedQuantity):
    def __init__(self, field, x) -> None:
        super().__init__(field)
        self.x = x
        self.title = f"{field} value {x:.2e}"

    def compute(self):
        return self.function(self.x)


my_model = F.Simulation()

l_pyc = 33e-6
l_sic = 66e-6
pyc = F.Material(id=1, D_0=1.274e-7, E_D=0, borders=[0, l_pyc])
sic = F.Material(id=2, D_0=2.622e-11, E_D=0, borders=[l_pyc, l_pyc + l_sic])
my_model.materials = [pyc, sic]

vertices = np.concatenate(
    [
        np.linspace(0, l_pyc, num=500),
        np.linspace(l_pyc, l_pyc + l_sic, num=500),
    ]
)
my_model.mesh = F.MeshFromVertices(vertices)

my_model.T = F.Temperature(1000)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=50.7079, field=0),
    F.DirichletBC(surfaces=2, value=0, field=0),
]

my_model.dt = F.Stepsize(0.2)
my_model.settings = F.Settings(
    absolute_tolerance=1e-12,
    relative_tolerance=1e-50,
    final_time=50,
    chemical_pot=False,
)

derived_quantities = F.DerivedQuantities(
    [
        PointValue(field="solute", x=l_pyc + 15.75e-6),
        PointValue(field="solute", x=20e-6),
    ],
    filename="./results.csv",
)
xdmf_exports = [F.XDMFExport("solute", checkpoint=False)] + [derived_quantities]

my_model.exports = xdmf_exports
my_model.initialise()
my_model.run()
