# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample data (replace with your actual data)
np.random.seed(0)
screen_on_time = np.random.uniform(0, 10, 100)  # in hours
battery_drain = np.random.uniform(0, 100, 100)  # in percentage

# Create a pandas DataFrame
data = pd.DataFrame({
    'Screen On Time (hours)': screen_on_time,
    'Battery Drain (%)': battery_drain
})

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['Screen On Time (hours)'], data['Battery Drain (%)'])

# Set plot title and labels
plt.title('Scatter Plot of Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')

# Show grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_9e58cd29.png')