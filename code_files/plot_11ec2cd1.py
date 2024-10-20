# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Average Data Usage': [100, 120, 150, 180, 200, 220, 250, 280]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Age' and calculate the mean of 'Average Data Usage'
average_usage_by_age = df.groupby('Age')['Average Data Usage'].mean()

# Create a bar plot
plt.figure(figsize=(10, 6))
average_usage_by_age.plot(kind='bar')
plt.title('Average Data Usage by Age')
plt.xlabel('Age')
plt.ylabel('Average Data Usage')
plt.show()
plt.savefig('png_files/plot_11ec2cd1.png')