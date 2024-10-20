import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Screen On Time (hours)': [2, 4, 6, 8, 10, 12, 14, 16],
    'Battery Drain (%)': [10, 20, 30, 40, 50, 60, 70, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Screen On Time (hours)'], df['Battery Drain (%)'])

# Set title and labels
plt.title('Scatter Plot of Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours)')
plt.ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_02bfeb02.png')