import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Select the numeric features
numeric_features = df[['app_usage', 'screen_on_time', 'battery_drain', 'data_usage', 'cpu_usage', 'memory_usage']]

# Calculate the correlation matrix
corr_matrix = numeric_features.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()
plt.savefig('png_files/plot_4e631f32.png')