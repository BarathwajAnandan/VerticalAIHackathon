import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Group by Age and calculate average data usage
avg_data_usage_by_age = df.groupby('Age')['Data Usage'].mean()

# Create a bar plot
plt.figure(figsize=(10,6))
avg_data_usage_by_age.plot(kind='bar')
plt.title('Average Data Usage by Age')
plt.xlabel('Age')
plt.ylabel('Average Data Usage')
plt.show()
plt.savefig('png_files/plot_801e1a33.png')