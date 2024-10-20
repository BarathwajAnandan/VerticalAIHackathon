import matplotlib.pyplot as plt
import numpy as np

# Sample data
user_behavior_classes = ['Normal', 'Heavy', 'Light']
battery_drains = [10, 20, 5]

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(user_behavior_classes, battery_drains, color='skyblue')

# Set plot title and labels
plt.title('Average Battery Drain by User Behavior Class')
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain (mAh)')

# Add a legend
plt.legend(labels=['Normal', 'Heavy', 'Light'], loc='upper right')

# Show the plot
plt.show()
```

However, if you have more complex data and want to perform some analysis, you can use the pandas library to handle the data and the seaborn library to create the bar plot.

```
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data
data = {
    'User Behavior Class': ['Normal', 'Heavy', 'Light', 'Normal', 'Heavy', 'Light'],
    'Average Battery Drain (mAh)': [10, 20, 5, 12, 22, 6]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='User Behavior Class', y='Average Battery Drain (mAh)', data=df, color='skyblue')

# Set plot title and labels
plt.title('Average Battery Drain by User Behavior Class')
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain (mAh)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_8c95e68d.png')