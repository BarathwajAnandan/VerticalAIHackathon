# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6', 'Apple Watch', 'OnePlus 9'],
    'Average App Usage Time (minutes)': [120, 150, 100, 90, 110]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Device Model'], df['Average App Usage Time (minutes)'], color='skyblue')

# Set title and labels
plt.title('Average App Usage Time by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Average App Usage Time (minutes)')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
plt.savefig('png_files/plot_7cc31433.png')