import matplotlib.pyplot as plt

# Sample dataset
screen_on_time = [30, 60, 90, 120, 150, 180, 210, 240]
battery_drain = [10, 20, 30, 40, 50, 60, 70, 80]

# Create the scatter plot
plt.scatter(screen_on_time, battery_drain)

# Add title and labels
plt.title('Scatter Plot of Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (%)')

# Display the plot
plt.show()
plt.savefig('png_files/plot_cad33872.png')