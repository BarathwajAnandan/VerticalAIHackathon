# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace with your actual data)
data = {
    'App Usage (hours)': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    'Screen On Time (hours)': [4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    'Battery Drain (%)': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Data Usage (GB)': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CPU Usage (%)': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_dc9bffcf.png')