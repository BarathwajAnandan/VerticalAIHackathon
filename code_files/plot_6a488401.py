import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Group by 'User Behavior Class' and calculate the average 'Battery Drain'
avg_battery_drain = df.groupby('User Behavior Class')['Battery Drain'].mean()

# Create a bar plot
plt.figure(figsize=(10,6))
avg_battery_drain.plot(kind='bar')
plt.title('Average Battery Drain by User Behavior Class')
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain')
plt.show()
plt.savefig('png_files/plot_6a488401.png')