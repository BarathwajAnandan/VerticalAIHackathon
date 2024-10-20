import matplotlib.pyplot as plt
import numpy as np

# Generate random data (replace with actual data if available)
np.random.seed(0)
screen_on_time = np.random.uniform(0, 10, 50)  # 50 random values between 0 and 10 hours
battery_drain = np.random.uniform(0, 100, 50)  # 50 random values between 0 and 100%

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(screen_on_time, battery_drain)

# Set title and labels
plt.title('Scatter Plot of Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_3745753f.png')