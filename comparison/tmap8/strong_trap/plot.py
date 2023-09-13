import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("results/derived_quantities.csv", delimiter=",", names=True)

t = data["ts"]
flux = -data["Flux_surface_2_solute"]

plt.plot(t, flux)
plt.show()