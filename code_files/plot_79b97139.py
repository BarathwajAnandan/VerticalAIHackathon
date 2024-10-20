# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Create a density plot of battery drain by gender
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x='battery_drain', hue='gender', fill=True, shade=True)
plt.title('Density Plot of Battery Drain by Gender')
plt.xlabel('Battery Drain Time (hours)')
plt.ylabel('Density')
plt.legend(title='Gender')
plt.show()
plt.savefig('png_files/plot_79b97139.png')