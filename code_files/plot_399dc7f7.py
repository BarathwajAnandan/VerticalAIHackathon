import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6', 'Apple Watch Series 7', 'OnePlus 9 Pro'],
    'Average Battery Drain (hours)': [5.2, 6.1, 4.8, 3.5, 5.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Device Model'], df['Average Battery Drain (hours)'], color='skyblue')

# Set chart title and labels
plt.title('Average Battery Drain by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Average Battery Drain (hours)')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
plt.savefig('png_files/plot_399dc7f7.png')