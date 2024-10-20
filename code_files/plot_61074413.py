# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Generate random data for Age and Screen On Time
ages = np.random.randint(18, 80, 100)  # Random ages between 18 and 80
on_times = np.random.randint(1, 24, 100)  # Random on times between 1 and 24 hours

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(ages, on_times, color='skyblue', alpha=0.8)

# Add title and labels
plt.title('Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Show grid and legend
plt.grid(True)
plt.legend(['Random Data', 'Actual Data'])

# Display the plot
plt.show()
plt.savefig('png_files/plot_61074413.png')