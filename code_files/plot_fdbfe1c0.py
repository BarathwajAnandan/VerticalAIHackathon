# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Operating System': ['Android', 'iOS', 'Android', 'iOS', 'Android', 'iOS', 'Android', 'iOS', 'Android', 'iOS'],
    'App Usage Time (minutes)': [120, 90, 100, 110, 130, 105, 115, 95, 125, 108],
    'Screen On Time (minutes)': [180, 150, 160, 170, 190, 165, 175, 155, 185, 168]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
for os in df['Operating System'].unique():
    os_df = df[df['Operating System'] == os]
    plt.scatter(os_df['App Usage Time (minutes)'], os_df['Screen On Time (minutes)'], label=os)

# Set plot title and labels
plt.title('Scatter Plot of App Usage Time vs. Screen On Time by Operating System')
plt.xlabel('App Usage Time (minutes)')
plt.ylabel('Screen On Time (minutes)')

# Add legend
plt.legend()

# Show the plot
plt.show()
plt.savefig('png_files/plot_fdbfe1c0.png')