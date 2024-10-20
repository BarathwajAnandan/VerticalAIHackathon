import matplotlib.pyplot as plt
import numpy as np

# Sample data for app usage time in minutes per day
app_usage_time = np.array([
    30, 45, 60, 90, 120, 30, 45, 60, 90, 120,  # Social Media
    15, 30, 45, 60, 90, 15, 30, 45, 60, 90,    # Productivity
    60, 90, 120, 180, 240, 60, 90, 120, 180, 240,  # Games
    10, 20, 30, 40, 50, 10, 20, 30, 40, 50      # Utilities
])

# Create a histogram
plt.hist(app_usage_time, bins=10, edgecolor='black')

# Set the title and labels
plt.title('Histogram of App Usage Time (min/day)')
plt.xlabel('App Usage Time (min/day)')
plt.ylabel('Frequency')

# Show the plot
plt.show()
plt.savefig('png_files/plot_acfcd8f6.png')