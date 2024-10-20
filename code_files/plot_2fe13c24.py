# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(0)
data = {
    'User Behavior': np.random.choice(['Normal', 'Aggressive', 'Indifferent'], 100),
    'Battery Drain (hours)': np.random.uniform(0, 2, 100)
}
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='User Behavior', y='Battery Drain (hours)', data=df)

# Add labels and title
plt.title('Box Plot of Battery Drain by User Behavior Class')
plt.xlabel('User Behavior')
plt.ylabel('Battery Drain (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_2fe13c24.png')