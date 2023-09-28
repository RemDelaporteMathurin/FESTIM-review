import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('results/derived_quantities.csv', delimiter=',', names=True)


x_positions = [0, 10, 12]
time = data['ts']
for x_pos in x_positions:
    mobile_concentration = data[f"solute_value_{x_pos:.2e}".replace('+', '').replace('.', '')]
    plt.plot(time, mobile_concentration, label=f'$x = {x_pos}$ m')

plt.legend()
plt.show()
