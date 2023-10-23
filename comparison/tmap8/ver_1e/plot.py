import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("results.csv", names=True, delimiter=",")
data_tmap8 = np.genfromtxt("ver-1e_out.csv", names=True, delimiter=",")

for i, x_pos in enumerate([20e-6, 48.8e-6]):
    mobile_conc_festim = data[
        f"solute_value_{x_pos:.2e}".replace("+", "").replace(".", "").replace("-", "")
    ]
    plt.plot(
        data["ts"],
        mobile_conc_festim,
        color="tab:blue",
        label="FESTIM",
        zorder=1,
        linewidth=3,
    )
    plt.plot(
        data_tmap8["time"],
        data_tmap8[f"conc_point{i+1}"],
        color="tab:orange",
        linestyle="solid",
        label="TMAP8",
        zorder=2,
        alpha=0.85,
    )

    plt.annotate(
        f"$x={x_pos*1e6} $ μm",
        (data_tmap8["time"][-1] + 1, mobile_conc_festim[-1]),
        va="center",
    )

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# plt.xlim(left=0)
plt.ylim(bottom=0)
plt.gca().spines[["right", "top"]].set_visible(False)
plt.grid(True, which="major", alpha=0.3)

plt.xlabel("Time (s)")
plt.ylabel("Mobile concentration")
plt.tight_layout()

for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"ver-1e-results.{ext}")
plt.show()

# import netCDF4

# nc = netCDF4.Dataset('ver-1e_out.e')
# print(nc.variables.keys())
# x = np.array(nc.variables['coordx'])

# u_at_all_times = np.array(nc.variables['vals_nod_var1'])

# for u in u_at_all_times[::10]:
#     plt.plot(x, u)

# plt.show()
