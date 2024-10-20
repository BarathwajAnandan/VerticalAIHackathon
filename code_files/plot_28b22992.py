# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data = {
    'App Usage': [10, 20, 30, 40, 50],
    'Screen On Time': [5, 10, 15, 20, 25],
    'Battery Drain': [20, 15, 10, 5, 0],
    'Data Usage': [100, 200, 300, 400, 500],
    'Other Feature': [10, 20, 30, 40, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()
plt.savefig('png_files/plot_28b22992.png')