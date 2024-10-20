# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung S22', 'Google Pixel 6', 'OnePlus 9', 'Huawei P30'],
    'Average App Usage Time (minutes)': [120, 90, 100, 110, 130]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Device Model'], df['Average App Usage Time (minutes)'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Bar Plot of Average App Usage Time by Device Model')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_f4aab0cc.png')