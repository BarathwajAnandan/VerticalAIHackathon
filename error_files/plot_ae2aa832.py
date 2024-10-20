# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(0)
data = {
    'Screen On Time (hours)': np.random.uniform(0, 10, 100),
    'Battery Drain (mAh)': np.random.uniform(0, 1000, 100),
    'Correlation Coefficient': np.random.uniform(-1, 1, 100)
}

df = pd.DataFrame(data)

# Calculate the correlation coefficient
correlation_coefficient = df['Screen On Time (hours)'].corr(df['Battery Drain (mAh)'])

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True)
plt.title('Correlation between Screen On Time and Battery Drain')
plt.show()

# Plot the correlation between Screen On Time and Battery Drain
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Screen On Time (hours)', y='Battery Drain (mAh)', data=df)
plt.title('Correlation between Screen On Time and Battery Drain')
plt.show()

# Plot the correlation between Screen On Time and Correlation Coefficient
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Screen On Time (hours)', y='Correlation Coefficient', data=df)
plt.title('Correlation between Screen On Time and Correlation Coefficient')
plt.show()
```

This code will create three plots:

1. A heatmap of the correlation between all variables in the dataset.
2. A scatter plot of the correlation between Screen On Time and Battery Drain.
3. A scatter plot of the correlation between Screen On Time and the Correlation Coefficient.

Please note that the actual data should be used instead of the sample data provided in the code.

Also, you can use `seaborn`'s `pairplot` function to create a heatmap of the correlation between all variables in the dataset.

```
plt.figure(figsize=(8, 6))
sns.pairplot(df, vars=['Screen On Time (hours)', 'Battery Drain (mAh)'], hue='Correlation Coefficient', palette='coolwarm')
plt.title('Correlation between Screen On Time and Battery Drain')
plt.show()
plt.savefig('png_files/plot_ae2aa832.png')