import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'iPhone 12', 'Google Pixel 6', 'OnePlus 9 Pro'],
    'App Usage Time (hours)': [120, 100, 90, 80, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by App Usage Time in descending order
df = df.sort_values(by='App Usage Time (hours)', ascending=False)

# Select the top 5 device models
top_5_devices = df.head(5)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_5_devices['Device Model'], top_5_devices['App Usage Time (hours)'])
plt.xlabel('Device Model')
plt.ylabel('App Usage Time (hours)')
plt.title('Top 5 Device Models by App Usage Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_9adee93d.png')