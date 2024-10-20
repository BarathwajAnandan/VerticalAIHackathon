import matplotlib.pyplot as plt

# Sample data
user_behavior_classes = {
    'Class A': 120,
    'Class B': 90,
    'Class C': 80,
    'Class D': 70,
    'Class E': 60
}

# Sort the data by value in descending order
sorted_classes = sorted(user_behavior_classes.items(), key=lambda x: x[1], reverse=True)

# Select the top 3 classes
top_classes = sorted_classes[:3]

# Extract the class names and usage times
class_names = [class_name for class_name, _ in top_classes]
usage_times = [usage_time for _, usage_time in top_classes]

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(usage_times, labels=class_names, autopct='%1.1f%%')
plt.title('Top 3 User Behavior Classes by App Usage Time')
plt.show()
plt.savefig('png_files/plot_6f5ed483.png')