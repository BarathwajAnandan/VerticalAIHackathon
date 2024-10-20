# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data (replace with your actual data)
np.random.seed(0)
data = {
    'Screen On Time (minutes)': np.random.randint(30, 120, 20),
    'Battery Drain (%)': np.random.uniform(10, 30, 20)
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Screen On Time (minutes)'], df['Battery Drain (%)'])

# Set title and labels
plt.title('Scatter Plot of Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (%)')

# Show grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_56eba04f.png')