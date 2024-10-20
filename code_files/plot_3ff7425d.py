# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'User ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Class': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}
df = pd.DataFrame(data)

# Count the occurrences of each class
class_counts = df['Class'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Class Distribution of User Behavior')
plt.show()
plt.savefig('png_files/plot_3ff7425d.png')