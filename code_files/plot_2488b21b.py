import matplotlib.pyplot as plt
import numpy as np

# Data usage for males and females
male_data_usage = np.array([10, 15, 8, 12, 18, 11, 9, 13, 16, 14])
female_data_usage = np.array([8, 10, 7, 9, 12, 11, 6, 8, 10, 13])

# Create a figure and axis
fig, ax = plt.subplots()

# Create the box plot
ax.boxplot([male_data_usage, female_data_usage], labels=['Male', 'Female'])

# Set the title and labels
ax.set_title('Box Plot of Data Usage by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Data Usage (GB)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_2488b21b.png')