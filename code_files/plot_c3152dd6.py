# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Generate a random dataset
screen_on_time = np.random.randint(30, 120, 100)  # minutes
gender = np.random.choice(['Male', 'Female'], 100)  # gender

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time], 
            labels=['Male', 'Female'], 
            whis='mid')

# Set title and labels
plt.title('Screen On Time by Gender')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Time (minutes)')

# Show the plot
plt.show()
```

This code will generate a box plot with two boxes, one for male and one for female screen on times. The 'whis' parameter is set to 'mid' to display the interquartile range (IQR) of the data, which represents the middle 50% of the data.

You can customize the plot further by adding more features, such as:

* Adding a legend
* Changing the colors or markers
* Adding a horizontal line to separate the two boxes
* Using different colors for the boxes
* Adding a title or labels to the plot

Here's an example with some of these customizations:

```
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Generate a random dataset
screen_on_time = np.random.randint(30, 120, 100)  # minutes
gender = np.random.choice(['Male', 'Female'], 100)  # gender

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time, screen_on_time], 
            labels=['Male', 'Female'], 
            whis='mid')

# Set title and labels
plt.title('Screen On Time by Gender')
plt.xlabel('Screen On Time (minutes)')
plt.ylabel('Time (minutes)')

# Add a legend
plt.legend(labels=['Male', 'Female'], loc='upper right')

# Show the plot
plt.show()
plt.savefig('png_files/plot_c3152dd6.png')