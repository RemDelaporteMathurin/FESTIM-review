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

plt.bar_label(barfestim, padding=8, fmt='%.1f s', fontsize=14)
plt.bar_label(bartmap, padding=8, fmt='%.1f s', fontsize=14)

plt.gca().set_yticks(ypos + width/2, labels=labels)
plt.gca().set_xticks([])

plt.legend()
plt.gca().spines[['left', 'right', 'top', 'bottom']].set_visible(False)
plt.tight_layout()
plt.show()