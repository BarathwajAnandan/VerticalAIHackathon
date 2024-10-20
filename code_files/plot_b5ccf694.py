import matplotlib.pyplot as plt

# Data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
data_usage = [80, 120, 90, 60, 40, 20]

# Create the figure and axis
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(age_groups, data_usage)

# Set title and labels
ax.set_title('Data Usage by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Data Usage (GB)')

# Show the values on top of each bar
for i, value in enumerate(data_usage):
    ax.text(i, value + 3, str(value), ha='center', va='bottom')

# Show the plot
plt.show()
plt.savefig('png_files/plot_b5ccf694.png')