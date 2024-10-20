import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
ages = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
data_usage = np.random.randint(100, 500, size=(6, 10))  # 6 age groups, 10 samples each

# Calculate average data usage for each age group
avg_data_usage = np.mean(data_usage, axis=1)

# Create a pandas DataFrame
df = pd.DataFrame({'Age': ages, 'Average Data Usage (MB)': avg_data_usage})

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Age'], df['Average Data Usage (MB)'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Average Data Usage (MB)')
plt.title('Average Data Usage by Age')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure labels fit within the plot area
plt.show()
plt.savefig('png_files/plot_7851fda0.png')