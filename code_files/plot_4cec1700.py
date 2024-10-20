# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'User Behavior': ['User A', 'User B', 'User C', 'User D', 'User E', 'User F', 'User G', 'User H', 'User I'],
    'Battery Drain (mAh)': [10, 12, 15, 8, 18, 20, 12, 15, 8],
    'Time (minutes)': [30, 45, 60, 90, 120, 180, 210, 240, 270]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate average battery drain
df['Average Battery Drain (mAh)'] = df['Battery Drain (mAh)'] / df['Time (minutes)']

# Group by User Behavior and calculate average battery drain
average_battery_drain_by_user_behavior = df.groupby('User Behavior')['Average Battery Drain (mAh)'].mean()

# Create a bar plot
plt.figure(figsize=(10, 6))
average_battery_drain_by_user_behavior.plot(kind='bar')
plt.title('Average Battery Drain by User Behavior')
plt.xlabel('User Behavior')
plt.ylabel('Average Battery Drain (mAh)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_4cec1700.png')