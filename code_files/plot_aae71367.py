import matplotlib.pyplot as plt

# Data
genders = ['Male', 'Female', 'Other']
counts = [60, 30, 10]

# Create a pie chart
plt.pie(counts, labels=genders, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
plt.savefig('png_files/plot_aae71367.png')