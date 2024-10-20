import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate random data for demonstration purposes
np.random.seed(0)
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Data Usage (GB)': np.random.normal(10, 5, size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Data Usage (GB)'], 
             df.loc[df['Gender'] == 'Female', 'Data Usage (GB)']], 
            labels=['Male', 'Female'])

# Set title and labels
plt.title('Box Plot of Data Usage by Gender')
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_9bbee3fa.png')