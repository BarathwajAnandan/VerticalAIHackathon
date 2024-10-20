import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Data Usage (GB)': [10.2, 8.5, 12.1, 9.8, 11.5, 7.2, 10.8, 9.2, 11.2, 8.8]
}

df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Data Usage (GB)'], 
             df.loc[df['Gender'] == 'Female', 'Data Usage (GB)']], 
            labels=['Male', 'Female'])
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')
plt.show()
plt.savefig('png_files/plot_4cf83d4d.png')