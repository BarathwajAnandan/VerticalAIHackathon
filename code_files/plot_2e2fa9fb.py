import matplotlib.pyplot as plt

# Sample data
device_models = ['iPhone 13', 'Samsung Galaxy S22', 'Google Pixel 6', 'OnePlus 9 Pro', 'iPhone 12']
model_counts = [120, 80, 60, 40, 20]

# Create a pie chart
plt.pie(model_counts, labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
plt.savefig('png_files/plot_2e2fa9fb.png')