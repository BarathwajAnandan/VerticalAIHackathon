import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Device Model': ['iPhone 13', 'iPhone 13', 'iPhone 12', 'iPhone 12', 'Samsung S22', 'Samsung S22', 'Google Pixel 6', 'Google Pixel 6'],
    'App Usage Time (minutes)': [120, 90, 100, 80, 110, 130, 90, 100]
}
df = pd.DataFrame(data)

# Group by Device Model and calculate average App Usage Time
avg_usage_time = df.groupby('Device Model')['App Usage Time (minutes)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(avg_usage_time['Device Model'], avg_usage_time['App Usage Time (minutes)'])
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by Device Model')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure labels fit within the plot area
plt.show()
plt.savefig('png_files/plot_ce8315ac.png')