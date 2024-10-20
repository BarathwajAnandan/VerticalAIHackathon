import matplotlib.pyplot as plt
import numpy as np

# Data
operating_systems = ['Windows', 'MacOS', 'Android', 'iOS']
num_apps = [1000, 500, 2000, 1500]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(operating_systems, num_apps, color='skyblue')

# Set title and labels
plt.title('Number of Apps Installed by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
plt.savefig('png_files/plot_6fa837b7.png')