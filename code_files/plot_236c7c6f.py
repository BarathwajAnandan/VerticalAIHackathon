# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Screen On Time (minutes)': np.random.randint(30, 120, 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Screen On Time (minutes)' to numeric values
df['Screen On Time (minutes)'] = pd.to_numeric(df['Screen On Time (minutes)'])

# Create a box plot of screen on time by gender
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'], 
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)']],
            labels=['Male', 'Female'])
plt.title('Box Plot of Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')
plt.show()
plt.savefig('png_files/plot_236c7c6f.png')