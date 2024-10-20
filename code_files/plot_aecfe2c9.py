# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'App Usage Time (minutes)': [30, 45, 60, 90, 120, 30, 45, 60, 90, 120,
                                 20, 35, 50, 70, 90, 20, 35, 50, 70, 90]
}
df = pd.DataFrame(data)

# Group by 'Gender' and calculate the box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'App Usage Time (minutes)'].values,
             df.loc[df['Gender'] == 'Female', 'App Usage Time (minutes)'].values],
            labels=['Male', 'Female'])
plt.title('Box Plot of App Usage Time by Gender')
plt.xlabel('Gender')
plt.ylabel('App Usage Time (minutes)')
plt.show()
plt.savefig('png_files/plot_aecfe2c9.png')