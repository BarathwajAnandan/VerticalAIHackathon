# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone', 'Samsung', 'Google Pixel', 'Apple Watch', 'Xiaomi Redmi'],
    'Average App Usage Time (minutes)': [30, 45, 60, 20, 25]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by device model and calculate average usage time
avg_usage_time = df.groupby('Device Model')['Average App Usage Time (minutes)'].mean()

# Create a bar plot
plt.figure(figsize=(10, 6))
avg_usage_time.plot(kind='bar')
plt.title('Average App Usage Time by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_97656903.png')