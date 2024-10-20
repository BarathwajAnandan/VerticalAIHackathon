# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Device_Model': ['iPhone 13', 'Samsung S22', 'Google Pixel 6', 'iPhone 13', 'Samsung S22', 'Google Pixel 6',
                     'iPhone 13', 'Samsung S22', 'Google Pixel 6', 'iPhone 13', 'Samsung S22', 'Google Pixel 6'],
    'App_Usage_Time': np.random.uniform(10, 60, 12)
}
df = pd.DataFrame(data)

# Group by device model and calculate average app usage time
average_usage = df.groupby('Device_Model')['App_Usage_Time'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(average_usage['Device_Model'], average_usage['App_Usage_Time'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by Device Model')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_fe82219d.png')