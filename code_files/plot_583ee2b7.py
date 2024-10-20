bash
pip install pandas seaborn matplotlib
```

### Load Libraries and Sample Data

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'App Usage': [10, 20, 30, 40, 50],
    'Screen On Time': [5, 10, 15, 20, 25],
    'Battery Drain': [20, 15, 10, 5, 0],
    'Data Usage': [100, 200, 300, 400, 500],
    'RAM Usage': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
```

### Create Correlation Matrix

```
# Calculate correlation matrix
corr_matrix = df.corr()

# Print correlation matrix
print(corr_matrix)
```

### Create Correlation Heatmap

```
# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)

# Set title and labels
plt.title('Correlation Heatmap of Numeric Features')
plt.xlabel('Features')
plt.ylabel('Features')

# Show plot
plt.show()
plt.savefig('png_files/plot_583ee2b7.png')