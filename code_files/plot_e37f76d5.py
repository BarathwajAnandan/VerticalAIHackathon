# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
data = {
    'app_usage': np.random.uniform(0, 100, 100),
    'screen_on_time': np.random.uniform(0, 120, 100),
    'battery_drain': np.random.uniform(0, 10, 100),
    'data_usage': np.random.uniform(0, 100, 100),
    'time_spent': np.random.uniform(0, 120, 100),
    'battery_level': np.random.uniform(0, 100, 100)
}

df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_e37f76d5.png')