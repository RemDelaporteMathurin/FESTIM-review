import numpy as np
import matplotlib.pyplot as plt

data_festim = np.genfromtxt("results/derived_quantities.csv", delimiter=",", names=True)
data_tmap8 = np.genfromtxt("ver-1c_csv.csv", delimiter=",", names=True)

x_positions = [0, 10, 12]
for x_pos in x_positions:
    mobile_concentration = data_festim[
        f"solute_value_{x_pos:.2e}".replace("+", "").replace(".", "")
    ]
    plt.plot(data_festim["ts"], mobile_concentration, color="tab:blue", label="FESTIM")

    plt.plot(
        data_tmap8["time"],
        data_tmap8[f"point{x_pos}"],
        linestyle="dashed",
        color="tab:orange",
        label="TMAP8",
    )

    plt.annotate(
        f"$x = {x_pos}$ m",
        (data_tmap8["time"][-1] + 2, data_tmap8[f"point{x_pos}"][-1]),
        va="center",
        ha="left",
    )

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.xlim(left=0)
plt.ylim(bottom=0)
plt.gca().spines[["right", "top"]].set_visible(False)
plt.grid(True, which="major", alpha=0.3)

plt.xlabel("Time (s)")
plt.ylabel("Mobile concentration (H/m$^3$)")
for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"ver-1c-results.{ext}")
plt.show()
