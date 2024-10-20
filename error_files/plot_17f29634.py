import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'User Behavior Class': ['New User', 'Active User', 'Inactive User'],
    'Average App Usage Time (minutes)': [30, 60, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['User Behavior Class'], df['Average App Usage Time (minutes)'], color='skyblue')

# Set labels and title
plt.xlabel('User Behavior Class')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by User Behavior Class')

# Show the legend and plot
plt.legend()
plt.show()
```

This code will generate a simple bar chart with the user behavior class on the x-axis and the average app usage time on the y-axis.

If you want to add more features to your chart, such as error bars or a grid, you can use the following code:

```
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'User Behavior Class': ['New User', 'Active User', 'Inactive User'],
    'Average App Usage Time (minutes)': [30, 60, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart with error bars
plt.figure(figsize=(8, 6))
plt.bar(df['User Behavior Class'], df['Average App Usage Time (minutes)'], color='skyblue', yerr=np.array([5, 10, 3]))

# Set labels and title
plt.xlabel('User Behavior Class')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by User Behavior Class')

# Show the legend and plot
plt.legend()
plt.grid(True)
plt.show()
```

This code will generate a bar chart with error bars representing the standard deviation of the data.

You can also use Seaborn library to create a more visually appealing chart:

```
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data
data = {
    'User Behavior Class': ['New User', 'Active User', 'Inactive User'],
    'Average App Usage Time (minutes)': [30, 60, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart with Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='User Behavior Class', y='Average App Usage Time (minutes)', data=df, color='skyblue')

# Set labels and title
plt.xlabel('User Behavior Class')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by User Behavior Class')

# Show the legend and plot
plt.legend()
plt.show()
plt.savefig('png_files/plot_17f29634.png')