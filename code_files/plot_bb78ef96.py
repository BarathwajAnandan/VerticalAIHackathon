import matplotlib.pyplot as plt
import numpy as np

# Data
data_male = np.array([1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200])
data_female = np.array([800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600])

# Create box plot
plt.boxplot([data_male, data_female], labels=['Male', 'Female'])

# Set title and labels
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (MB)')

# Show plot
plt.show()
plt.savefig('png_files/plot_bb78ef96.png')