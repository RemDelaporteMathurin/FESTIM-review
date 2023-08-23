import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("results/permeation_flux.csv", delimiter=",", names=True)

plt.plot(data["ts"], data["Flux_surface_2_solute"])
plt.savefig("out.png")
plt.show()
