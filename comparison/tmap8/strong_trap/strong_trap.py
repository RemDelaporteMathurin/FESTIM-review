import festim as F
import numpy as np
import scipy.constants as const

my_model = F.Simulation()

my_model.mesh = F.MeshFromVertices(
    vertices=np.linspace(0, 1E-3, num=1001)
)
my_model.materials = F.Material(id=1, D_0=1.9e-7, E_D=0.2)
my_model.T = F.Temperature(value=1000)

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=1, value=5.3e+21,field=0),
    F.DirichletBC(surfaces=2, value=0, field=0)
]
rho_n=6.338E28

trap = F.Trap(
            k_0=2.62e-17,
            E_k=0.2,
            p_0=1e13,
            E_p=2.5,
            density=1E-3*rho_n,
            materials=my_model.materials.materials[0]
        )

my_model.traps = [trap]
my_model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    final_time=1E6  # s
    )

class CustomStepsize(F.Stepsize):
    def adapt(self, t, nb_it, converged):
        change_ratio = self.adaptive_stepsize["stepsize_change_ratio"]
        dt_min = self.adaptive_stepsize["dt_min"]
        stepsize_stop_max = self.adaptive_stepsize["stepsize_stop_max"]
        t_stop = self.adaptive_stepsize["t_stop"]
        if not converged:
            self.value.assign(float(self.value) / change_ratio)
            if float(self.value) < dt_min:
                raise ValueError("stepsize reached minimal value")
        if nb_it < 5:
            self.value.assign(float(self.value) * change_ratio)
        else:
            self.value.assign(float(self.value) / change_ratio)

        if t_stop is not None:
            if t_stop[0] <= t < t_stop[1]:
                if float(self.value) > stepsize_stop_max:
                    self.value.assign(stepsize_stop_max)

my_model.dt = CustomStepsize(initial_value=1E-1,
    dt_min=1E-3,
    stepsize_change_ratio=1.2,
    t_stop=[0.25e6, 0.4e6],
    stepsize_stop_max=1E3
    )
derived_quantities = F.DerivedQuantities([F.HydrogenFlux(surface=2)], filename="results/derived_quantities.csv")


my_model.exports = [derived_quantities]

my_model.initialise()
my_model.run()