import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'User Behavior Class': ['Active', 'Inactive', 'Moderate', 'New'],
    'Proportion of Users': [40, 20, 30, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['Proportion of Users'], labels=df['User Behavior Class'], autopct='%1.1f%%')
plt.title('Proportion of Users by User Behavior Class')
plt.show()
plt.savefig('png_files/plot_2ce991c0.png')