import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(0)
age = np.random.randint(18, 80, 100)
screen_on_time = np.random.randint(1, 24, 100)

# Create a DataFrame
df = pd.DataFrame({'Age': age, 'Screen On Time': screen_on_time})

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Screen On Time'])

# Add title and labels
plt.title('Scatter Plot of Age vs. Screen On Time')
plt.xlabel('Age')
plt.ylabel('Screen On Time (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_a3da70c3.png')