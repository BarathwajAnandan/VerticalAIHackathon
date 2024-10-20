import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data (replace with your own data)
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Usage Time (min)': [30, 45, 60, 90, 120, 150, 180]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Usage Time (min)'], bins=10, edgecolor='black')

# Set title and labels
plt.title('Histogram of App Usage Time (min/day)')
plt.xlabel('Usage Time (min)')
plt.ylabel('Frequency')

# Show the plot
plt.show()
plt.savefig('png_files/plot_5085ba6d.png')