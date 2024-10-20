# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Screen On Time (hours)': np.random.uniform(2, 10, 100),
    'Battery Drain (%)': np.random.uniform(10, 90, 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Screen On Time (hours)'], df['Battery Drain (%)'])

# Add title and labels
plt.title('Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_4b3cddb9.png')