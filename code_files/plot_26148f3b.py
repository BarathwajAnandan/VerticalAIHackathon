# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(0)
data = {
    'App Usage': np.random.uniform(0, 1, 100),
    'Screen On Time': np.random.uniform(0, 1, 100),
    'Battery Drain': np.random.uniform(0, 1, 100),
    'Data Usage': np.random.uniform(0, 1, 100),
    'App Performance': np.random.uniform(0, 1, 100),
    'Battery Life': np.random.uniform(0, 1, 100)
}

df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_26148f3b.png')