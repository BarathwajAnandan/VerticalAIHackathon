import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Age': [18, 18, 18, 25, 25, 25, 30, 30, 30],
    'Data Usage (MB)': [1000, 1200, 1100, 1500, 1800, 1600, 2000, 2200, 2100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by Age and calculate average Data Usage
average_data_usage = df.groupby('Age')['Data Usage (MB)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_data_usage['Age'], average_data_usage['Data Usage (MB)'], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Average Data Usage (MB)')
plt.title('Average Data Usage by Age')
plt.xticks(average_data_usage['Age'])
plt.show()
plt.savefig('png_files/plot_62d95240.png')