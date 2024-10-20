import matplotlib.pyplot as plt

# Sample data
data_usage = {
    'Male': [10, 12, 11],
    'Female': [8, 9, 7]
}

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(data_usage.keys(), data_usage.values())

# Set labels and title
plt.xlabel('Gender')
plt.ylabel('Data Usage (GB)')
plt.title('Data Usage by Gender')

# Show the chart
plt.show()
plt.savefig('png_files/plot_4ccca8b7.png')