# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([20, 21, 19, 22, 20, 23, 21, 19, 22, 20, 24])
average_usage = np.array([10, 15, 8, 12, 11, 18, 14, 9, 13, 12, 16])

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(ages, average_usage, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Average Data Usage')
plt.title('Average Data Usage by Age')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.show()
```

This code will generate a bar plot with the age on the x-axis and the average data usage on the y-axis. The `plt.xticks(rotation=90)` line is used to rotate the x-axis labels by 90 degrees, making them easier to read.

**Example Use Case:**

You can replace the `ages` and `average_usage` arrays with your own data to create a bar plot of average data usage by age. For example, if you have a CSV file `data.csv` containing the following data:

| Age | Average Data Usage |
| --- | --- |
| 20  | 10                |
| 21  | 15                |
| 19  | 8                 |
| 22  | 12                |
| 20  | 11                |
| 23  | 18                |
| 21  | 14                |
| 19  | 9                 |
| 22  | 13                |
| 20  | 12                |
| 24  | 16                |

You can use the following code to generate the bar plot:

```
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('user_behavior_dataset.csv')

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(data['Age'], data['Average Data Usage'], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Average Data Usage')
plt.title('Average Data Usage by Age')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_e73d4183.png')