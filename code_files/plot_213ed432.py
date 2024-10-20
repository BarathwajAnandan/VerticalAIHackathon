# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the operating systems and their corresponding app counts
operating_systems = {
    'Windows': 1000,
    'macOS': 500,
    'Linux': 300,
    'Android': 200,
    'iOS': 150
}

# Create a list of operating systems
os_list = list(operating_systems.keys())

# Create a list of app counts for each operating system
app_counts = [operating_systems[os] for os in os_list]

# Create a bar plot
plt.bar(os_list, app_counts)

# Set the title and labels
plt.title('Number of Apps Installed by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')

# Show the plot
plt.show()
plt.savefig('png_files/plot_213ed432.png')