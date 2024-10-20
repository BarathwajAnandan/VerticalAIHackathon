import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([18, 25, 30, 35, 40, 45, 50, 55, 60])
data_usage = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(ages, data_usage, color='skyblue')

# Set title and labels
plt.title('Average Data Usage by Age')
plt.xlabel('Age')
plt.ylabel('Average Data Usage (GB)')

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
```

However, if you want to create a bar plot with actual average data usage by age, you would need to have the actual data. Here's an example of how you can create a bar plot with actual data using the pandas library to read the data from a CSV file.

```
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from a CSV file
data = pd.read_csv('user_behavior_dataset.csv')

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(data['Age'], data['Average Data Usage (GB)'], color='skyblue')

# Set title and labels
plt.title('Average Data Usage by Age')
plt.xlabel('Age')
plt.ylabel('Average Data Usage (GB)')

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_feaf1659.png')