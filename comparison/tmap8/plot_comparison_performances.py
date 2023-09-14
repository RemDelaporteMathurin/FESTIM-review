import matplotlib.pyplot as plt
import json
import numpy as np


with open("comparison_results.json") as f:
    data = json.load(f)

width = 0.4

labels = list(data.keys())
ypos = np.arange(len(labels))
festim_times = [case['festim'] for case in data.values()]
tmap8_times = [case['tmap'] for case in data.values()]

bartmap = plt.barh(ypos + width, tmap8_times, width, label='TMAP8')
barfestim = plt.barh(ypos, festim_times, width, label='FESTIM')

plt.bar_label(barfestim, padding=8, fmt='%.1f s', fontsize=10, color=barfestim.patches[0].get_facecolor())
plt.bar_label(bartmap, padding=8, fmt='%.1f s', fontsize=10, color=bartmap.patches[0].get_facecolor())

plt.gca().set_yticks(ypos + width/2, labels=labels)
plt.gca().set_xticks([20, 40, 60])

plt.legend(bbox_to_anchor=(0.7, 1.1), frameon=False, ncol=2)
plt.gca().spines[['left', 'right', 'top', 'bottom']].set_visible(False)
plt.grid(True, which='major', axis="x", alpha=0.3)
plt.xlabel("Execution time (s)")
plt.tight_layout()
for ext in ["png", "svg", "pdf"]:
    plt.savefig(f"tmap8_comparison_results.{ext}")
plt.show()