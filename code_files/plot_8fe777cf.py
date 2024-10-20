import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
screen_on_time = np.array([60, 90, 30, 120, 45, 75, 90, 60, 30, 120, 45, 75])

# Create a histogram
plt.hist(screen_on_time, bins=10, edgecolor='black')

# Set title and labels
plt.title('Histogram of Screen On Time')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Frequency')

# Show the plot
plt.show()
plt.savefig('png_files/plot_8fe777cf.png')