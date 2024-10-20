# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame with numeric features
np.random.seed(0)
data = {
    'App Usage': np.random.uniform(0, 100, 100),
    'Screen On Time': np.random.uniform(0, 100, 100),
    'Battery Drain': np.random.uniform(0, 100, 100),
    'Data Usage': np.random.uniform(0, 100, 100),
    'RAM Usage': np.random.uniform(0, 100, 100)
}
df = pd.DataFrame(data)

# Calculate the correlation matrix
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_15f7e056.png')