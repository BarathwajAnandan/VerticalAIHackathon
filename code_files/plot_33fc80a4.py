# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Screen On Time (hours)': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Battery Drain (%)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Screen On Time (hours)'], df['Battery Drain (%)'])

# Add title and labels
plt.title('Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_33fc80a4.png')