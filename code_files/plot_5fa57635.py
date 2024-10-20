# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(0)
data = {
    'Screen On Time (hours)': np.random.uniform(0, 10, 100),
    'Battery Drain (mAh)': np.random.uniform(0, 5000, 100),
    'Correlation Coefficient': np.random.uniform(-1, 1, 100)
}

df = pd.DataFrame(data)

# Calculate the correlation coefficient
correlation_coefficient = df['Screen On Time (hours)'].corr(df['Battery Drain (mAh)'])

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Between Screen On Time and Battery Drain')
plt.show()

# Plot the correlation between screen on time and battery drain
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Screen On Time (hours)', y='Battery Drain (mAh)', data=df)
plt.title('Correlation Between Screen On Time and Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (mAh)')
plt.show()

# Plot the correlation heatmap with screen on time on the x-axis
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Screen On Time (hours)', y='Battery Drain (mAh)', data=df)
plt.scatter(df['Screen On Time (hours)'], df['Battery Drain (mAh)'], c=df['Correlation Coefficient'], cmap='coolwarm')
plt.colorbar(label='Correlation Coefficient')
plt.title('Correlation Between Screen On Time and Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (mAh)')
plt.show()
plt.savefig('png_files/plot_5fa57635.png')