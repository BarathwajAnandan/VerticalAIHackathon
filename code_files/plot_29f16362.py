import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.array([18, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52])
data_usage = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

# Calculate average data usage
average_data_usage = np.mean(data_usage)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(ages, data_usage, color='skyblue')
plt.title('Average Data Usage by Age')
plt.xlabel('Age')
plt.ylabel('Average Data Usage (GB)')
plt.xticks(ages)
plt.yticks(np.arange(0, average_data_usage + 10, 5))
plt.grid(True)
plt.axhline(y=average_data_usage, color='red', linestyle='--', label='Average')
plt.legend()
plt.show()
plt.savefig('png_files/plot_29f16362.png')