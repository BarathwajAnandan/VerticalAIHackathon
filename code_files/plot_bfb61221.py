import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'User Behavior': ['New User', 'Active User', 'Inactive User', 'New User', 'Active User', 'Inactive User'],
    'Number of Apps': [10, 20, 15, 8, 12, 18]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['User Behavior'], df['Number of Apps'], color='skyblue')

# Set labels and title
plt.xlabel('User Behavior')
plt.ylabel('Number of Apps')
plt.title('Bar Chart of Number of Apps Installed by User Behavior Class')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_bfb61221.png')