# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Age': np.random.randint(18, 60, 100),
    'Screen On Time (hours)': np.random.uniform(2, 12, 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Screen On Time (hours)'])

# Add title and labels
plt.title('Scatter Plot of Age vs. Screen On Time')
plt.xlabel('Age (years)')
plt.ylabel('Screen On Time (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_fcee3811.png')