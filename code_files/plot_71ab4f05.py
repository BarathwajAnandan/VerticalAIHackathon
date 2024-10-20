# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([25, 31, 42, 28, 35, 29, 38, 32, 40, 27])
apps_installed = np.array([10, 15, 20, 12, 18, 14, 22, 16, 25, 11])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(ages, apps_installed, color='blue', marker='o')

# Set title and labels
plt.title('Scatter Plot of Age vs. Number of Apps Installed')
plt.xlabel('Age')
plt.ylabel('Number of Apps Installed')

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_71ab4f05.png')