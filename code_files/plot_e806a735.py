import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Screen On Time (minutes)': [120, 150, 180, 200, 220, 90, 110, 130, 140, 160,
                                 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
}

df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'].values,
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)'].values],
            labels=['Male', 'Female'])
plt.title('Box Plot of Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')
plt.show()
plt.savefig('png_files/plot_e806a735.png')