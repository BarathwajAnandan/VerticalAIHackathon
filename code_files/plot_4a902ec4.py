# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the data
screen_on_times = np.random.uniform(1, 24, 100)  # in minutes
battery_drains = np.random.uniform(0, 100, 100)  # in milliamps

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(screen_on_times, battery_drains, s=2, alpha=0.8, color='blue')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (mA)')
plt.title('Screen On Time vs. Battery Drain')
plt.grid(True)
plt.show()
```

This code will generate a scatter plot with screen on time on the x-axis and battery drain on the y-axis. The `np.random.uniform` function is used to generate random data for both variables. The `s=2` parameter in the `plt.scatter` function makes the points slightly larger, and the `alpha=0.8` parameter makes the points slightly transparent, giving a more realistic representation of the data.

You can customize the plot further by adding more features, such as:

* Adding a regression line to the plot
* Adding a legend to the plot
* Changing the colors and styles of the plot
* Adding more data points to the plot

Here's an example of how you can modify the code to add a regression line:

```
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the data
screen_on_times = np.random.uniform(1, 24, 100)  # in minutes
battery_drains = np.random.uniform(0, 100, 100)  # in milliamps

# Calculate the regression line
z = np.polyfit(screen_on_times, battery_drains, 1)
p = np.poly1d(z)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(screen_on_times, battery_drains, s=2, alpha=0.8, color='blue')
plt.plot(screen_on_times, p(screen_on_times), color='red', linewidth=2)
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Battery Drain (mA)')
plt.title('Screen On Time vs. Battery Drain')
plt.grid(True)
plt.show()
plt.savefig('png_files/plot_4a902ec4.png')