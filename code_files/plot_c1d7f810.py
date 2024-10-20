# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Screen On Time (minutes)': np.random.randint(30, 120, size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'], 
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)']], 
            labels=['Male', 'Female'])

# Set title and labels
plt.title('Box Plot of Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_c1d7f810.png')