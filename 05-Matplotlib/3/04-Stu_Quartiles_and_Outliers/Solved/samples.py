# Dependencies
import matplotlib.pyplot as plt
import numpy as np


arr = [8, 8, 12, 24, 54, 54, 75, 78, 98, 102, 132]
x_axis = np.arange(0, len(arr), 1)

# Calculate the indices for the lower and upper quartiles
lower_quartile_index = (len(arr) + 1) // 4
upper_quartile_index = 3 * len(arr) // 4

# Retrieve the lower and upper quartiles
lower_quartile = arr[lower_quartile_index]
upper_quartile = arr[upper_quartile_index]

# Calculate the interquartile range
iqr = upper_quartile - lower_quartile

# Create axes for the included and excluded data
included = arr[lower_quartile_index:upper_quartile_index]
included_axis = np.arange(lower_quartile_index, upper_quartile_index, 1)

excluded_low = arr[0:lower_quartile_index]
low_axis = np.arange(0, len(excluded_low), 1)

excluded_high = arr[upper_quartile_index:len(arr)]
high_axis = np.arange(len(included) + len(excluded_high), len(arr), 1)

# Create a plot displaying included and excluded data
fig, ax = plt.subplots()
fig.suptitle("Interquartile Range Example", fontsize=16, fontweight="bold")

ax.plot(included_axis, included, marker='o', color='b', label="IQR")
ax.scatter(
    low_axis,
    excluded_low,
    marker='o',
    color='r',
    label="Excluded (Low)")
ax.scatter(
    high_axis,
    excluded_high,
    marker='o',
    color='r',
    label="Excluded (High)")

plt.legend(loc="upper left", fancybox=True)
plt.show()

# Report descriptions of the data
print("The lowr quartile of the data is {}.".format(lower_quartile))
print("The upper quartile of the data is {}.".format(upper_quartile))
print("The interquartile range of the data is {}.".format(iqr))
