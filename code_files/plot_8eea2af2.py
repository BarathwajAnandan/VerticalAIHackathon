# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Operating System': ['Windows', 'Windows', 'MacOS', 'MacOS', 'Linux', 'Linux', 'Windows', 'Windows', 'MacOS', 'MacOS'],
    'User Behavior Class': ['Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by Operating System and User Behavior Class, then count the occurrences
grouped_df = df.groupby(['Operating System', 'User Behavior Class']).size().reset_index(name='Count')

# Pivot the DataFrame to get the desired format
pivoted_df = grouped_df.pivot(index='Operating System', columns='User Behavior Class', values='Count')

# Plot the bar chart
pivoted_df.plot(kind='bar', figsize=(10, 6))
plt.title('Distribution of User Behavior Classes by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Count')
plt.legend(title='User Behavior Class')
plt.show()
plt.savefig('png_files/plot_8eea2af2.png')