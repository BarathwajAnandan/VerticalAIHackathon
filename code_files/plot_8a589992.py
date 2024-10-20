# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Data Usage (GB)': [10, 15, 12, 18, 20, 22, 25, 30, 35, 40,
                       8, 12, 15, 18, 20, 22, 25, 28, 30, 32]
}
df = pd.DataFrame(data)

# Group by 'Gender' and calculate the 'Data Usage (GB)'
grouped_df = df.groupby('Gender')['Data Usage (GB)'].describe()

# Print the grouped DataFrame
print(grouped_df)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Data Usage (GB)'].values,
             df.loc[df['Gender'] == 'Female', 'Data Usage (GB)'].values],
            labels=['Male', 'Female'])
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')
plt.show()
plt.savefig('png_files/plot_8a589992.png')