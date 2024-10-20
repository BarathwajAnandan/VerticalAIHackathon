# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Device_Model': ['iPhone 13', 'iPhone 12', 'Samsung S22', 'Samsung S21', 'Google Pixel 6', 'Google Pixel 5'],
    'App_Usage_Time': [120, 100, 110, 90, 130, 105]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Device_Model' and calculate the average 'App_Usage_Time'
average_usage_time = df.groupby('Device_Model')['App_Usage_Time'].mean().reset_index()

# Sort the data in descending order of average usage time
average_usage_time = average_usage_time.sort_values(by='App_Usage_Time', ascending=False)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_usage_time['Device_Model'], average_usage_time['App_Usage_Time'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.title('Average App Usage Time by Device Model')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure labels fit within the plot area
plt.show()
plt.savefig('png_files/plot_5eb195fa.png')