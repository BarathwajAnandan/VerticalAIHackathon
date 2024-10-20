import matplotlib.pyplot as plt
import numpy as np

# Sample data for battery drain across different age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
battery_drain_data = {
    '18-24': np.random.normal(50, 10, 100),
    '25-34': np.random.normal(55, 12, 100),
    '35-44': np.random.normal(60, 15, 100),
    '45-54': np.random.normal(65, 18, 100),
    '55+': np.random.normal(70, 20, 100)
}

# Create a figure and axis
fig, ax = plt.subplots()

# Create a box plot for each age group
ax.boxplot([battery_drain_data[age_group] for age_group in age_groups],
           labels=age_groups)

# Set title and labels
ax.set_title('Battery Drain Distribution Across Different Age Groups')
ax.set_xlabel('Age Group')
ax.set_ylabel('Battery Drain (%)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_4c386879.png')