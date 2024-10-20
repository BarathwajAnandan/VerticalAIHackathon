import matplotlib.pyplot as plt
import numpy as np

# Data for user behavior classes
user_behavior_classes = ['Active', 'Inactive', 'Engaged', 'Not Engaged', 'New User']
class_distribution = [35, 20, 25, 10, 10]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(user_behavior_classes, class_distribution, color='skyblue')
plt.xlabel('User Behavior Class')
plt.ylabel('Distribution (%)')
plt.title('Bar Chart of User Behavior Class Distribution')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the percentage value on top of each bar
for i, value in enumerate(class_distribution):
    plt.text(i, value + 1, str(value) + '%', ha='center')

plt.tight_layout()  # Ensure labels fit within the figure
plt.show()
plt.savefig('png_files/plot_e74fe6d0.png')