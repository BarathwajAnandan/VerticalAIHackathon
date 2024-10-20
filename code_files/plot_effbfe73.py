import matplotlib.pyplot as plt

# Sample data
device_models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
distributions = [25, 30, 20, 15, 10]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(distributions, labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
```

In this code:

- We import the `matplotlib.pyplot` module, which provides functions for creating a variety of charts, including pie charts.
- We define a list of device models and their corresponding distributions.
- We create a pie chart using `plt.pie()`, passing in the distributions and device models as arguments. The `autopct` parameter is used to display the percentage value of each slice.
- We set the title of the chart using `plt.title()`.
- Finally, we display the chart using `plt.show()`.

When you run this code, it will generate a pie chart displaying the distribution of device models.

### Customizing the Pie Chart

You can customize the pie chart further by using various options available in the `plt.pie()` function. Here are a few examples:

- **Color scheme**: You can specify a custom color scheme using the `colors` parameter. For example:
  ```
plt.pie(distributions, labels=device_models, colors=['red', 'green', 'blue', 'yellow', 'purple'])
```
- **Start angle**: You can specify the start angle of the pie chart using the `startangle` parameter. For example:
  ```
plt.pie(distributions, labels=device_models, startangle=90)
```
- **Radius**: You can specify the radius of the pie chart using the `radius` parameter. For example:
  ```
plt.pie(distributions, labels=device_models, radius=1.2)
```

### Pie Chart with Multiple Series

If you want to display multiple series of data on the same pie chart, you can use the `plt.pie()` function with multiple arguments. Here's an example:

```
import matplotlib.pyplot as plt

# Sample data
device_models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
distributions1 = [25, 30, 20, 15, 10]
distributions2 = [15, 20, 25, 20, 10]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie([distributions1, distributions2], labels=device_models, autopct='%1.1f%%', radius=1.2)
plt.title('Device Model Distribution')
plt.show()
plt.savefig('png_files/plot_effbfe73.png')