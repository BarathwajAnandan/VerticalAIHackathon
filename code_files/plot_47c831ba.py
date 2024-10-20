# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 60],
    'Data Usage (GB)': [10, 15, 20, 25, 30, 35, 40, 45, 50]
}
df = pd.DataFrame(data)

# Calculate average data usage by age group
df['Age Group'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60], labels=['20-29', '30-39', '40-49', '50-59'])
average_usage = df.groupby('Age Group')['Data Usage (GB)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_usage['Age Group'], average_usage['Data Usage (GB)'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Average Data Usage (GB)')
plt.title('Average Data Usage by Age Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_47c831ba.png')