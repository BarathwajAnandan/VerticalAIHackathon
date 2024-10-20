# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Device Model': ['Model A', 'Model B', 'Model C', 'Model A', 'Model B', 'Model C', 'Model A', 'Model B', 'Model C'],
    'Battery Drain (mAh)': [100, 120, 90, 110, 130, 80, 105, 140, 85]
}
df = pd.DataFrame(data)

# Group by device model and calculate the battery drain
grouped_df = df.groupby('Device Model')['Battery Drain (mAh)'].describe()

# Print the grouped DataFrame
print(grouped_df)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Device Model'] == 'Model A', 'Battery Drain (mAh)'].values,
             df.loc[df['Device Model'] == 'Model B', 'Battery Drain (mAh)'].values,
             df.loc[df['Device Model'] == 'Model C', 'Battery Drain (mAh)'].values],
            labels=['Model A', 'Model B', 'Model C'])
plt.title('Box Plot of Battery Drain by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Battery Drain (mAh)')
plt.show()
plt.savefig('png_files/plot_73ccf75a.png')