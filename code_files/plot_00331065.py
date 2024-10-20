import matplotlib.pyplot as plt
import numpy as np

# Data
operating_systems = ['Windows', 'MacOS', 'Linux']
behavior_classes = ['Active', 'Inactive', 'Moderate']

# Data for each operating system
windows_data = [25, 30, 45]
macos_data = [20, 35, 45]
linux_data = [30, 25, 45]

# Create a figure and axis
fig, ax = plt.subplots()

# Set the width of the bars
bar_width = 0.2

# Set the x positions of the bars
x = np.arange(len(operating_systems))

# Create the stacked bar plot
ax.bar(x - bar_width, windows_data, bar_width, label='Windows')
ax.bar(x, macos_data, bar_width, label='MacOS')
ax.bar(x + bar_width, linux_data, bar_width, label='Linux')

# Set the title and labels
ax.set_title('Stacked Bar Plot of User Behavior Class by Operating System')
ax.set_xlabel('Operating System')
ax.set_ylabel('Percentage of Users')

# Set the x ticks
ax.set_xticks(x)
ax.set_xticklabels(operating_systems)

# Add a legend
ax.legend()

# Show the plot
plt.show()
plt.savefig('png_files/plot_00331065.png')