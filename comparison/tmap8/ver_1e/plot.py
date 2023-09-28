import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("results.csv", names=True, delimiter=",")
print(data.dtype.names)
plt.plot(data["ts"], data["solute_value_488e05"])
plt.show()
