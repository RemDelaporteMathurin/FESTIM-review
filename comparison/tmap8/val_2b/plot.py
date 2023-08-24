import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("results/derived_quantities.csv", names=True, delimiter=",")

t = data["ts"]
temp1 = data["Average_T_volume_1"]
temp2 = data["Average_T_volume_2"]

desorption_flux = -2*data["Flux_surface_1_solute"]

data_tmap8 = np.genfromtxt("results/tmap8_results.csv", names=True, delimiter=",")

t_tmap8 = data_tmap8["time"]
idx_tmap8 = np.where(t_tmap8 > 182400)
temp1_tmap8 = data_tmap8["Temp"]

scaling_factor = 1e20
desorption_flux_tmap8 = 2*data_tmap8["avg_flux_left"] * scaling_factor

data_tmap8_short_timestep = np.genfromtxt("results/tmap8_results.csv", names=True, delimiter=",")

t_tmap8_short_timestep = data_tmap8_short_timestep["time"]
idx_tmap8_short_timestep = np.where(t_tmap8 > 182400)
temp1_tmap8_short_timestep = data_tmap8_short_timestep["Temp"]

scaling_factor = 1e20
desorption_flux_tmap8_short_timestep = 2*data_tmap8_short_timestep["avg_flux_left"] * scaling_factor

data_loading = np.genfromtxt("results/derived_quantities_loading.csv", names=True, delimiter=",")

t_loading = data_loading["ts"]
temp1_loading = data_loading["Average_T_volume_1"]
temp2_loading = data_loading["Average_T_volume_2"]

plt.plot(temp1, desorption_flux)
# plt.plot(temp1_tmap8[idx_tmap8], desorption_flux_tmap8[idx_tmap8])
plt.plot(temp1_tmap8_short_timestep[idx_tmap8_short_timestep], desorption_flux_tmap8_short_timestep[idx_tmap8])
plt.show()
