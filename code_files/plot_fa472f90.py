# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Data Usage (GB)': [10, 20, 15, 30, 25, 12, 18, 22, 28, 32,
                        8, 12, 15, 18, 20, 22, 25, 28, 30, 32]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Data Usage (GB)'].values,
             df.loc[df['Gender'] == 'Female', 'Data Usage (GB)'].values],
            labels=['Male', 'Female'])
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')
plt.show()
plt.savefig('png_files/plot_fa472f90.png')