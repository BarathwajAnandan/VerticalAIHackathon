import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6', 'OnePlus 9', 'Huawei P30', 'iPhone 12', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 8', 'Huawei P20'],
    'Number of Users': [1000, 800, 700, 600, 500, 400, 300, 200, 100, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Device Model' and sum the 'Number of Users'
df_grouped = df.groupby('Device Model')['Number of Users'].sum().reset_index()

# Sort the DataFrame by 'Number of Users' in descending order
df_sorted = df_grouped.sort_values(by='Number of Users', ascending=False)

# Select the top 5 device models
top_5_devices = df_sorted.head(5)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_5_devices['Device Model'], top_5_devices['Number of Users'], color='skyblue')
plt.xlabel('Device Model')
plt.ylabel('Number of Users')
plt.title('Top 5 Device Models by Number of Users')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_cbfb4293.png')