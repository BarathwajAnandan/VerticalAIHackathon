import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
avg_usage_time = [120, 100, 90, 80, 60]  # in minutes

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(age_groups, avg_usage_time, marker='o')

# Set title and labels
ax.set_title('Average App Usage Time by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Average Usage Time (minutes)')

# Show grid lines
ax.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_b1a81770.png')