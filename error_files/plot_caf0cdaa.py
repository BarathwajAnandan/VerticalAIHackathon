import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60])
screen_on_time = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(ages, screen_on_time, color='blue', marker='o')

# Add title and labels
plt.title('Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Add grid lines
plt.grid(True)

# Show the plot
plt.show()
```

This code will generate a scatter plot with age on the x-axis and screen on time on the y-axis. Each point on the plot represents a sample data point.

If you want to create a more interactive plot, you can use a library like plotly.

```
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 60],
    'Screen On Time': [2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the scatter plot
fig = px.scatter(df, x='Age', y='Screen On Time', color='Age', hover_name='Age')

# Update the layout
fig.update_layout(title='Age vs. Screen On Time',
                  xaxis_title='Age',
                  yaxis_title='Screen On Time (hours)')

# Show the plot
fig.show()
plt.savefig('png_files/plot_caf0cdaa.png')