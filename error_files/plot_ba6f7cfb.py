# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Age': [20, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    'Screen On Time (hours)': [4.5, 5.2, 6.1, 7.3, 8.1, 9.2, 10.5, 11.8, 12.9, 14.1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Screen On Time (hours)'])

# Add title and labels
plt.title('Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Display the plot
plt.show()
```

This code will create a scatter plot with age on the x-axis and screen on time on the y-axis. The plot will display the relationship between age and screen on time.

If you want to add more features to the plot, such as a regression line or different colors for different groups, you can modify the code as follows:

```
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
data = {
    'Age': [20, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    'Screen On Time (hours)': [4.5, 5.2, 6.1, 7.3, 8.1, 9.2, 10.5, 11.8, 12.9, 14.1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age, df['Screen On Time (hours)'])

# Add a regression line
z = np.polyfit(df['Age'], df['Screen On Time (hours)'], 1)
p = np.poly1d(z)
plt.plot(df['Age'],p(df['Age']),"r--")

# Add title and labels
plt.title('Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Display the plot
plt.show()
plt.savefig('png_files/plot_ba6f7cfb.png')