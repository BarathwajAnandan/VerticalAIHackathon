import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6', 'iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6'],
    'App Usage Time (minutes)': [120, 90, 110, 130, 100, 105]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by device model and calculate average app usage time
average_usage = df.groupby('Device Model')['App Usage Time (minutes)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_usage['Device Model'], average_usage['App Usage Time (minutes)'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by Device Model')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_9992e70c.png')