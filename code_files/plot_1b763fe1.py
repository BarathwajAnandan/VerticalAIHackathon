# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Age': np.random.randint(18, 60, 100),
    'Screen On Time': np.random.randint(1, 24, 100)
}
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Screen On Time'])

# Add title and labels
plt.title('Scatter Plot of Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_1b763fe1.png')