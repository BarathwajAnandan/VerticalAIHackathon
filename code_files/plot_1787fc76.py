import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('user_behavior_dataset.csv')

# Calculate screen on time for each gender
screen_on_time_gender = df.groupby('Gender')['Screen On Time'].sum()

# Create a box plot of screen on time by gender
plt.figure(figsize=(10,6))
screen_on_time_gender.plot(kind='box')
plt.title('Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time')
plt.show()
plt.savefig('png_files/plot_1787fc76.png')