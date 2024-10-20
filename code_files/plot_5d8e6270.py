import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Screen On Time (hours)': [2.5, 3.2, 2.1, 2.8, 2.9, 3.1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Gender'], df['Screen On Time (hours)'], color='skyblue')

# Set labels and title
plt.xlabel('Gender')
plt.ylabel('Average Screen On Time (hours)')
plt.title('Average Screen On Time by Gender')

# Add annotations
for i, value in enumerate(df['Screen On Time (hours)']):
    plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')

# Show the plot
plt.show()
plt.savefig('png_files/plot_5d8e6270.png')