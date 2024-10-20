import matplotlib.pyplot as plt

# Sample data
device_models = {
    'iPhone 13': 120,
    'Samsung Galaxy S22': 150,
    'Google Pixel 6': 80,
    'OnePlus 9 Pro': 100,
    'Other': 50
}

# Extract device models and their counts
models = list(device_models.keys())
counts = list(device_models.values())

# Create a pie chart
plt.pie(counts, labels=models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
plt.savefig('png_files/plot_0356a7cb.png')