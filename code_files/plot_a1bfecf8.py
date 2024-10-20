import matplotlib.pyplot as plt
import numpy as np

# Sample data
screen_on_time = np.array([60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
battery_drain = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(screen_on_time, battery_drain, marker='o', color='blue', label='Screen On Time vs. Battery Drain')

# Add title and labels
plt.title('Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (%)')

# Add grid lines
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()
plt.savefig('png_files/plot_a1bfecf8.png')