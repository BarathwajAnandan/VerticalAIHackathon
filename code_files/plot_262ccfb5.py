# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'User Behavior Class': ['Class A', 'Class B', 'Class C', 'Class A', 'Class B', 'Class C'],
    'Battery Drain (mAh)': [100, 120, 110, 105, 125, 115]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'User Behavior Class' and calculate average 'Battery Drain (mAh)'
average_battery_drain = df.groupby('User Behavior Class')['Battery Drain (mAh)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(average_battery_drain['User Behavior Class'], average_battery_drain['Battery Drain (mAh)'])
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain (mAh)')
plt.title('Average Battery Drain by User Behavior Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_262ccfb5.png')