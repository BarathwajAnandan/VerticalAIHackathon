# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
data = {
    'App Usage': [10, 20, 15, 30, 25, 18, 22, 12, 28, 16],
    'Screen On Time': [60, 70, 55, 80, 65, 50, 75, 40, 85, 60],
    'Battery Drain': [5, 3, 8, 2, 6, 4, 9, 1, 7, 3],
    'Data Usage': [10, 15, 12, 20, 18, 15, 20, 12, 18, 15],
    'Time Spent on App': [30, 40, 35, 45, 38, 42, 40, 38, 42, 40],
    'Screen Resolution': [1920, 1080, 1600, 1440, 1280, 1600, 1440, 1280, 1600, 1440],
    'Processor Speed': [3.5, 3.2, 3.8, 3.1, 3.5, 3.2, 3.8, 3.1, 3.5, 3.2],
    'RAM': [8, 16, 32, 64, 8, 16, 32, 64, 8, 16]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert categorical variables to numerical variables
df['App Usage'] = pd.Categorical(df['App Usage']).codes
df['Screen On Time'] = pd.Categorical(df['Screen On Time']).codes
df['Battery Drain'] = pd.Categorical(df['Battery Drain']).codes
df['Data Usage'] = pd.Categorical(df['Data Usage']).codes

# Calculate correlation matrix
corr_matrix = df[['App Usage', 'Screen On Time', 'Battery Drain', 'Data Usage']].corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()
plt.savefig('png_files/plot_1e070716.png')