# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Usage': [10, 20, 15, 25, 12, 18, 20, 22, 18, 15]
}

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a box plot
ax.boxplot(data['Usage'], vert=False)

# Set title and labels
ax.set_title('Box Plot of Data Usage by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Usage')

# Show the plot
plt.show()
plt.savefig('png_files/plot_cfba8297.png')