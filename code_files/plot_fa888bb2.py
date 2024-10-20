# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Data_Usage': [10, 8, 12, 9, 11, 7, 13, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Gender' and calculate the average 'Data_Usage'
average_data_usage = df.groupby('Gender')['Data_Usage'].mean().reset_index()

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(average_data_usage['Gender'], average_data_usage['Data_Usage'], color=['blue', 'red'])
plt.xlabel('Gender')
plt.ylabel('Average Data Usage')
plt.title('Bar Chart of Average Data Usage by Gender')
plt.legend(['Average Data Usage'])
plt.show()
plt.savefig('png_files/plot_fa888bb2.png')