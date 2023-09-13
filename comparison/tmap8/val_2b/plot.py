import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("results/derived_quantities.csv", names=True, delimiter=",")

t = data["ts"]
temp1 = data["Average_T_volume_1"]
temp2 = data["Average_T_volume_2"]

desorption_flux = -2*data["Flux_surface_1_solute"]

data_tmap8 = np.genfromtxt("val-2b_out.csv", names=True, delimiter=",")

t_tmap8 = data_tmap8["time"]
idx_tmap8 = np.where(t_tmap8 > 182400)
temp1_tmap8 = data_tmap8["Temp"][idx_tmap8]

scaling_factor = 1e20
desorption_flux_tmap8 = 2*data_tmap8["avg_flux_left"] * scaling_factor
desorption_flux_tmap8 = desorption_flux_tmap8[idx_tmap8]

data_exp = np.genfromtxt("results/experimental_data.csv", names=True, delimiter=",")
temp_exp = data_exp["temp"]
flux_exp = data_exp["flux"] * 1e15  # tmap8 people scaled it

plt.plot(temp1, desorption_flux)
plt.plot(temp1_tmap8, desorption_flux_tmap8)
plt.scatter(temp_exp, flux_exp)
plt.show()
