# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'User Behavior Class': ['Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive'],
    'Age': [25, 30, 35, 20, 40, 28, 22, 38, 45, 32]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'User Behavior Class' and 'Gender', then count the number of users
gender_distribution = df.groupby(['User Behavior Class', 'Gender']).size().reset_index(name='Count')

# Pivot the DataFrame to get the desired format
gender_distribution_pivot = gender_distribution.pivot(index='User Behavior Class', columns='Gender', values='Count')

# Plot the pie chart
plt.figure(figsize=(10,6))
gender_distribution_pivot.plot(kind='pie', autopct='%1.1f%%', startangle=90, subplots=True)
plt.title('Gender Distribution by User Behavior Class')
plt.show()
plt.savefig('png_files/plot_0e49bb31.png')