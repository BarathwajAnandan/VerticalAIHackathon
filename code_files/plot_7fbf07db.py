import matplotlib.pyplot as plt

# Sample data
device_models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
device_counts = [10, 20, 30, 40, 50]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(device_counts, labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
plt.savefig('png_files/plot_7fbf07db.png')