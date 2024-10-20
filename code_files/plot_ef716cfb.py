import matplotlib.pyplot as plt

# Data for device model distribution
device_models = ['iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Huawei']
distribution = [30, 25, 20, 15, 10]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(distribution, labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
```

In this code:

1. We import the `matplotlib.pyplot` module, which provides functions for creating a variety of charts, including pie charts.
2. We define two lists: `device_models` and `distribution`. The `device_models` list contains the names of different device models, while the `distribution` list contains the corresponding distribution percentages.
3. We create a pie chart using the `plt.pie()` function, passing in the `distribution` list as the input data. We also specify the `labels` parameter to assign labels to each wedge of the pie chart.
4. We use the `autopct` parameter to format the value displayed on each wedge of the pie chart. In this case, we display the percentage value with one decimal place.
5. Finally, we set the title of the chart using `plt.title()` and display the chart using `plt.show()`.

When you run this code, it will generate a pie chart showing the distribution of different device models.

### Customizing the Pie Chart

You can customize the appearance of the pie chart by using various options available in the `plt.pie()` function. Here are a few examples:

*   To change the colors of the wedges, you can pass a list of colors to the `colors` parameter.
*   To explode a wedge from the center of the pie chart, you can pass a list of explosion values to the `explode` parameter.
*   To change the font size of the labels, you can use the `textprops` parameter.

Here's an updated code snippet that demonstrates these customizations:

```
import matplotlib.pyplot as plt

# Data for device model distribution
device_models = ['iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Huawei']
distribution = [30, 25, 20, 15, 10]

# Create a pie chart with customizations
plt.figure(figsize=(8, 8))
plt.pie(distribution, labels=device_models, autopct='%1.1f%%',
        colors=['#4CAF50', '#03A9F4', '#FF9800', '#2196F3', '#9C27B0'],
        explode=[0.1, 0, 0, 0, 0],
        textprops={'fontsize': 12})
plt.title('Device Model Distribution')
plt.show()
plt.savefig('png_files/plot_ef716cfb.png')