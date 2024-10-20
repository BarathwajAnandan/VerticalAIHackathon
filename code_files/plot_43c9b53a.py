import matplotlib.pyplot as plt
import numpy as np

# Generate random data for app usage time (min/day)
np.random.seed(0)
app_usage_time = np.random.normal(60, 20, 1000)  # mean 60, std 20, 1000 samples

# Create a histogram
plt.hist(app_usage_time, bins=20, alpha=0.7, color='skyblue', edgecolor='black')

# Set title and labels
plt.title('Histogram of App Usage Time (min/day)')
plt.xlabel('Usage Time (min/day)')
plt.ylabel('Frequency')

# Show the plot
plt.show()
plt.savefig('png_files/plot_43c9b53a.png')