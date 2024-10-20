import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Operating System': ['Windows', 'macOS', 'Linux', 'Chrome OS', 'Android'],
    'Screen On Time (hours)': [10.5, 12.8, 9.2, 8.5, 7.1]
}

# Sort the data by Screen On Time in descending order
sorted_data = sorted(data['Screen On Time (hours)'], reverse=True)
top_3_os = [os for os, time in zip(data['Operating System'], data['Screen On Time (hours)']) if time in sorted_data[:3]]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_3_os, [10.5, 12.8, 9.2])
plt.xlabel('Operating System')
plt.ylabel('Screen On Time (hours)')
plt.title('Top 3 Operating Systems by Screen On Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_8a79bc44.png')