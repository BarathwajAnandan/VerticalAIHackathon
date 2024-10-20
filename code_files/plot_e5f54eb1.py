import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
device_models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
average_screen_on_time = np.random.randint(2, 6, size=len(device_models))

# Create a pandas DataFrame
df = pd.DataFrame({
    'Device Model': device_models,
    'Average Screen On Time (hours)': average_screen_on_time
})

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Device Model'], df['Average Screen On Time (hours)'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Average Screen On Time (hours)')
plt.title('Bar Plot of Average Screen On Time by Device Model')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Add value labels on top of each bar
for i, value in enumerate(df['Average Screen On Time (hours)']):
    plt.text(i, value + 0.1, str(value), ha='center')

plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_e5f54eb1.png')