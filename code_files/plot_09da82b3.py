# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Device Model': ['Model A', 'Model A', 'Model A', 'Model A', 'Model A',
                     'Model B', 'Model B', 'Model B', 'Model B', 'Model B',
                     'Model C', 'Model C', 'Model C', 'Model C', 'Model C'],
    'Battery Drain': [10, 12, 11, 13, 9,
                      15, 18, 17, 19, 16,
                      8, 7, 9, 6, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([df.loc[df['Device Model'] == 'Model A', 'Battery Drain'],
             df.loc[df['Device Model'] == 'Model B', 'Battery Drain'],
             df.loc[df['Device Model'] == 'Model C', 'Battery Drain']],
            labels=['Model A', 'Model B', 'Model C'])
plt.title('Box Plot of Battery Drain by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Battery Drain')
plt.show()
```

This code will create a box plot with the device models on the x-axis and the battery drain values on the y-axis. Each box represents a device model, and the box plot displays the distribution of battery drain values for each model.

However, if you have a large dataset, it's more efficient to use the `seaborn` library, which is built on top of `matplotlib`. Here's an example:

```
# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Device Model': ['Model A', 'Model A', 'Model A', 'Model A', 'Model A',
                     'Model B', 'Model B', 'Model B', 'Model B', 'Model B',
                     'Model C', 'Model C', 'Model C', 'Model C', 'Model C'],
    'Battery Drain': [10, 12, 11, 13, 9,
                      15, 18, 17, 19, 16,
                      8, 7, 9, 6, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Device Model', y='Battery Drain', data=df)
plt.title('Box Plot of Battery Drain by Device Model')
plt.show()
plt.savefig('png_files/plot_09da82b3.png')