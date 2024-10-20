import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data for average app usage time by age group
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'Average App Usage Time (minutes)': [120, 110, 90, 80, 70, 60]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a line plot of average app usage time by age group
plt.figure(figsize=(10,6))
plt.plot(df['Age Group'], df['Average App Usage Time (minutes)'], marker='o')

# Set the title and labels
plt.title('Average App Usage Time by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average App Usage Time (minutes)')

# Show the grid lines
plt.grid(True)

# Show the plot
plt.show()
plt.savefig('png_files/plot_7bb27aee.png')