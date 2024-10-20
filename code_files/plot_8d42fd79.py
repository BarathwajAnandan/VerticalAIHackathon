import matplotlib.pyplot as plt

# Data
operating_systems = ['Windows', 'macOS', 'Linux', 'Android', 'iOS']
num_apps = [100, 80, 70, 120, 90]

# Create the figure and axis
fig, ax = plt.subplots()

# Create the bar plot
ax.bar(operating_systems, num_apps)

# Set title and labels
ax.set_title('Number of Apps Installed by Operating System')
ax.set_xlabel('Operating System')
ax.set_ylabel('Number of Apps')

# Show the plot
plt.show()
plt.savefig('png_files/plot_8d42fd79.png')