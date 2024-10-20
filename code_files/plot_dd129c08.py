import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'App Usage': [120, 90, 150, 180, 100],
    'Screen On Time': [180, 120, 200, 240, 150],
    'Battery Drain': [10, 8, 12, 15, 9],
    'Data Usage': [500, 300, 700, 1000, 400],
    'CPU Usage': [20, 15, 25, 30, 18],
    'Memory Usage': [30, 20, 35, 40, 25]
}
df = pd.DataFrame(data)

# Calculate correlations
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_dd129c08.png')