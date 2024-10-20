import matplotlib.pyplot as plt
import numpy as np

# Data for the number of apps installed by operating system
operating_systems = ['Windows', 'macOS', 'Linux', 'Android', 'iOS']
num_apps_installed = [1000, 800, 600, 1200, 900]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(operating_systems, num_apps_installed, color='skyblue')

# Set title and labels
plt.title('Number of Apps Installed by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps Installed')

# Add value labels on top of each bar
for i, value in enumerate(num_apps_installed):
    plt.text(i, value + 10, str(value), ha='center')

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_8c3584f5.png')