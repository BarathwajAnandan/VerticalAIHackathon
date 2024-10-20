# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([20, 22, 21, 19, 23, 20, 21, 18, 22, 19])
screen_on_time = np.array([4, 5, 4.5, 3.5, 5.5, 4, 4.5, 3, 5, 3.5])

# Create the scatter plot
plt.figure(figsize=(10,6))
plt.scatter(ages, screen_on_time, color='blue', marker='o')

# Add title and labels
plt.title('Scatter Plot of Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_3ef6aceb.png')