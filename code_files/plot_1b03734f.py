import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone 13', 'iPhone 13 Pro', 'iPhone 12', 'iPhone 12 Pro', 'iPhone 11', 'iPhone 11 Pro', 'iPhone 10', 'iPhone 10 Pro', 'iPhone 9', 'iPhone 9 Pro'],
    'Sales': [100, 50, 200, 150, 80, 120, 60, 90, 70, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by device model and calculate the percentage of sales
df_grouped = df.groupby('Device Model')['Sales'].sum().reset_index()

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(df_grouped['Sales'], labels=df_grouped['Device Model'], autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
plt.savefig('png_files/plot_1b03734f.png')