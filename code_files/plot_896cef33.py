import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Group the data by app and calculate the mean usage time
app_usage = df.groupby('app')['usage_time'].mean().reset_index()

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(app_usage['usage_time'], bins=10, edgecolor='black')
plt.xlabel('Usage Time (min/day)')
plt.ylabel('Frequency')
plt.title('Histogram of App Usage Time')
plt.xticks(rotation=90)
plt.show()
plt.savefig('png_files/plot_896cef33.png')