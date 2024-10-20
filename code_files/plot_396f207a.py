import matplotlib.pyplot as plt
import numpy as np

# Sample data
class_distribution = {
    'Freshman': 20,
    'Sophomore': 30,
    'Junior': 25,
    'Senior': 25
}

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(class_distribution.values(), labels=class_distribution.keys(), autopct='%1.1f%%')
plt.title('Class Distribution of Users')
plt.show()
```

In this code:

- We first import the necessary libraries, `matplotlib.pyplot` for creating the pie chart and `numpy` for numerical operations.
- We define a dictionary `class_distribution` to store the class distribution data.
- We create a pie chart using `plt.pie()` and pass the class distribution values as the first argument. We also pass the class distribution keys as the second argument to label each slice of the pie chart.
- We use `autopct` to display the percentage value of each slice.
- Finally, we display the pie chart using `plt.show()`.

When you run this code, it will generate a pie chart that visualizes the class distribution of users.

### Customizing the Pie Chart

You can customize the pie chart by using various options available in the `plt.pie()` function. Here are a few examples:

- To change the colors of the pie chart, you can pass a list of colors to the `colors` argument:
  ```
plt.pie(class_distribution.values(), labels=class_distribution.keys(), colors=['red', 'green', 'blue', 'yellow'])
```

- To change the radius of the pie chart, you can pass a value to the `radius` argument:
  ```
plt.pie(class_distribution.values(), labels=class_distribution.keys(), radius=1.2)
```

- To change the start angle of the pie chart, you can pass a value to the `startangle` argument:
  ```
plt.pie(class_distribution.values(), labels=class_distribution.keys(), startangle=90)
```

- To display a legend for the pie chart, you can pass a list of labels to the `labels` argument:
  ```
plt.pie(class_distribution.values(), labels=class_distribution.keys(), autopct='%1.1f%%', legend=True)
plt.savefig('png_files/plot_396f207a.png')