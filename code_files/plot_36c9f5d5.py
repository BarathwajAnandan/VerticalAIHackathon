# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
app_usage_data = {
    'App1': [10, 15, 8, 12, 18, 20, 22, 25, 28, 30],
    'App2': [12, 15, 10, 18, 20, 22, 25, 28, 30, 32],
    'App3': [8, 12, 10, 15, 18, 20, 22, 25, 28, 30]
}

# Create a histogram
plt.figure(figsize=(10, 6))
for app, data in app_usage_data.items():
    plt.hist(data, bins=10, alpha=0.7, color=plt.cm.tab20(np.linspace(0, 1, len(data))))
plt.title('Histogram of App Usage Time (min/day)')
plt.xlabel('App Usage Time (min)')
plt.ylabel('Frequency')
plt.xticks(np.arange(len(app_usage_data)), app_usage_data.keys())
plt.legend(title='Apps')
plt.show()
plt.savefig('png_files/plot_36c9f5d5.png')