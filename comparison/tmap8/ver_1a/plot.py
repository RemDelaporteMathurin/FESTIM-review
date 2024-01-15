from ver_1a import (
    my_model,
    derived_quantities,
    pressure_export,
    left_bc,
    right_flux,
    initial_pressure,
    R,
    avogadro,
    encl_surf,
    encl_vol,
    temperature,
    l,
)
from analytical_enclosure import (
    analytical_expression_fractional_release,
    cumulative_flux,
)
import numpy as np
from scipy.integrate import cumtrapz

# ------------ post processing ----------------

data_tmap8 = np.genfromtxt("ver-1a_csv.csv", delimiter=",", names=True)

t = derived_quantities.t
pressures = np.array(pressure_export.data)
fractional_release = 1 - pressures / initial_pressure
right_flux = np.abs(right_flux.data)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, fractional_release, linestyle="--", label="FESTIM")

times = np.linspace(0, my_model.settings.final_time, 1000)
analytical = analytical_expression_fractional_release(
    t=times,
    P_0=initial_pressure,
    D=my_model.materials.materials[0].D_0,
    S=left_bc.H_0,
    V=encl_vol,
    T=temperature,
    A=encl_surf,
    l=l,
)
plt.plot(times, analytical, label="analytical")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Fractional release")
plt.grid(alpha=0.3)

plt.figure()
plt.plot(t, right_flux)

plt.figure()

initial_quantity = initial_pressure * encl_vol / R / temperature * avogadro
cumulative_released = cumtrapz(right_flux, t, initial=0) * encl_surf

plt.plot(t, cumulative_released / initial_quantity, label="FESTIM", color='tab:blue')
plt.plot(data_tmap8["time"], data_tmap8["rhs_release"], label="TMAP8", linestyle="--", color='tab:orange')


analytical = cumulative_flux(
    t=times,
    P_0=initial_pressure,
    D=my_model.materials.materials[0].D_0,
    S=left_bc.H_0,
    V=encl_vol,
    T=temperature,
    A=encl_surf,
    l=l,
)
plt.plot(times, analytical, label="analytical", color="tab:green")

plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Cumulative relative release")
plt.grid(alpha=0.3)
plt.gca().spines[['right', 'top']].set_visible(False)
plt.ylim(bottom=0)
for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"ver-1a-results.{ext}")
plt.show()
