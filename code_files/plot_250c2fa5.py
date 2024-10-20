import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'User Behavior Class': ['Class A', 'Class B', 'Class C', 'Class A', 'Class B', 'Class C'],
    'Battery Drain': [10.2, 8.5, 12.1, 9.8, 7.9, 11.5]
}
df = pd.DataFrame(data)

# Group by User Behavior Class and calculate average battery drain
avg_battery_drain = df.groupby('User Behavior Class')['Battery Drain'].mean().reset_index()

# Create bar plot
plt.figure(figsize=(8, 6))
plt.bar(avg_battery_drain['User Behavior Class'], avg_battery_drain['Battery Drain'])
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain')
plt.title('Average Battery Drain by User Behavior Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_250c2fa5.png')