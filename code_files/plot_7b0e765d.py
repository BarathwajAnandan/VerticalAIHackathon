# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Screen On Time (minutes)': np.random.randint(30, 240, size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by gender and calculate statistics
grouped_df = df.groupby('Gender')['Screen On Time (minutes)'].describe()

# Print the grouped statistics
print(grouped_df)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'], 
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)']], 
            labels=['Male', 'Female'])
plt.title('Box Plot of Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')
plt.show()
plt.savefig('png_files/plot_7b0e765d.png')