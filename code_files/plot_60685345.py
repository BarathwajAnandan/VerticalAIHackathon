import matplotlib.pyplot as plt
import numpy as np

# Sample data: App usage time in minutes per day
app_usage_time = np.random.randint(1, 120, size=100)  # 100 random values between 1 and 120 minutes

# Create a histogram
plt.hist(app_usage_time, bins=10, edgecolor='black')

# Set title and labels
plt.title('Histogram of App Usage Time (min/day)')
plt.xlabel('App Usage Time (minutes)')
plt.ylabel('Frequency')

# Show the plot
plt.show()
plt.savefig('png_files/plot_60685345.png')