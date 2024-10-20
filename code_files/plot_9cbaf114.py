import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Data Usage (GB)': [10, 20, 15, 30, 25, 8, 12, 18, 22, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Data Usage (GB)'], 
             df.loc[df['Gender'] == 'Female', 'Data Usage (GB)']],
            labels=['Male', 'Female'],
            patch_artist=True)

# Set plot properties
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')
plt.show()
plt.savefig('png_files/plot_9cbaf114.png')