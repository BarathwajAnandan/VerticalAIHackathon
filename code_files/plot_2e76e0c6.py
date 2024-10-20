# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for battery drain and age
np.random.seed(0)
battery_drain = np.random.uniform(0, 10, 100)  # Random battery drain values between 0 and 10
age = np.random.uniform(1, 10, 100)  # Random age values between 1 and 10

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(age, battery_drain, marker='o', color='blue', label='Battery Drain vs. Age')

# Add title and labels
plt.title('Scatter Plot of Battery Drain vs. Age')
plt.xlabel('Age (years)')
plt.ylabel('Battery Drain (%)')

# Add legend
plt.legend()

# Show grid lines
plt.grid(True)

# Display the plot
plt.show()
```

This code will generate a scatter plot with age on the x-axis and battery drain on the y-axis. Each point on the plot represents a random battery drain value for a specific age.

If you want to use real data, you can replace the random data generation with your own data. For example, you can use a CSV file to load the data.

```
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('user_behavior_dataset.csv')

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Battery_Drain'])

# Add title and labels
plt.title('Scatter Plot of Battery Drain vs. Age')
plt.xlabel('Age (years)')
plt.ylabel('Battery Drain (%)')

# Show grid lines
plt.grid(True)

# Display the plot
plt.show()
plt.savefig('png_files/plot_2e76e0c6.png')