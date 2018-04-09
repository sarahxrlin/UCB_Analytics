# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy import stats

general_heights = pd.read_csv("../Resources/general_heights.csv")

wba_data = pd.read_csv("../Resources/wba_data.csv")
wba_heights = wba_data.iloc[:, -1]

(t_stat, p) = stats.ttest_ind(general_heights, wba_heights, equal_var=False)

# Report
print("The mean height of WBA players is {}.".format(wba_heights.mean()))
print("The mean height of women sampled is {}.".format(
    general_heights.values.mean()))

print("p is {}.".format(p[0]))
if p < 0.05:
    print("The difference in sample means is significant.")
else:
    print("The difference in sample means is not significant.")

# Plot sample means with error bars
tick_labels = ["General Public", "WBA Players"]

means = [general_heights.mean().values[0], wba_heights.mean()]
x_axis = np.arange(0, len(means))

sem = [general_heights.sem().values[0], wba_heights.sem()]

# Plot
fig, ax = plt.subplots()

fig.suptitle("Mean Height of Women in General Population and WBA Players",
             fontsize=12, fontweight="bold")

ax.errorbar(x_axis, means, yerr=sem, fmt="o")

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(64, 73)

ax.set_xticklabels(tick_labels)
ax.set_xticks([0, 1])

ax.set_ylabel("Height (Inches)")

plt.show()
