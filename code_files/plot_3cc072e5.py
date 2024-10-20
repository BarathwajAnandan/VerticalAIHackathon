import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
data = {
    'Screen On Time (minutes)': np.random.uniform(30, 240, 100),
    'Battery Drain (%)': np.random.uniform(10, 90, 100)
}

df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Screen On Time (minutes)'], df['Battery Drain (%)'])

# Add title and labels
plt.title('Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_3cc072e5.png')