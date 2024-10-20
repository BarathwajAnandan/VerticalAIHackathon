import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataset
data = {
    'Age': [18, 25, 30, 35, 40, 45, 50, 55, 60],
    'Screen On Time (hours)': [4.5, 6.2, 5.1, 4.8, 3.9, 3.2, 2.5, 2.1, 1.8]
}

# Convert the dataset to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Screen On Time (hours)'])

# Set the title and labels
plt.title('Scatter Plot of Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_7712e057.png')