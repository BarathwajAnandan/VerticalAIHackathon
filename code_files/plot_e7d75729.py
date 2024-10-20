# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Define a function to generate data
def generate_data():
    # Generate random screen on time and battery drain data
    screen_on_time = np.random.uniform(1, 24, 100)  # hours
    battery_drain = np.random.uniform(0, 100, 100)  # percentage
    return screen_on_time, battery_drain

# Generate data
screen_on_time, battery_drain = generate_data()

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(screen_on_time, battery_drain, color='blue', alpha=0.7)

# Add labels and title
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')
plt.title('Screen On Time vs. Battery Drain')
plt.grid(True)
plt.show()

# Save the plot to a file
plt.savefig('screen_on_time_vs_battery_drain.png')
plt.savefig('png_files/plot_e7d75729.png')