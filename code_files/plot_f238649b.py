import matplotlib.pyplot as plt

# Sample data
device_models = ['iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Huawei']
data_usage = [50, 60, 40, 55, 65]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(device_models, data_usage, color='skyblue')

# Set chart title and labels
plt.title('Data Usage by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Data Usage (GB)')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
```

This code will generate a simple bar chart with the device models on the x-axis and the corresponding data usage on the y-axis.

### Customizing the Chart

You can customize the chart further by adding more features, such as:

*   **Legend**: Add a legend to the chart to explain the colors used for each device model.
*   **Annotations**: Add annotations to the chart to provide more information about the data usage.
*   **Custom Colors**: Use custom colors for the bars and the chart background.

Here's an updated version of the code with these customizations:

```
import matplotlib.pyplot as plt

# Sample data
device_models = ['iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Huawei']
data_usage = [50, 60, 40, 55, 65]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(device_models, data_usage, color='#87CEEB')  # Custom color

# Set chart title and labels
plt.title('Data Usage by Device Model')
plt.xlabel('Device Model')
plt.ylabel('Data Usage (GB)')

# Add legend
plt.legend(labels=['iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Huawei'], loc='upper right')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations
plt.annotate('High usage', xy=(1, 60), xytext=(1, 70), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Low usage', xy=(3, 40), xytext=(3, 50), arrowprops=dict(facecolor='black', shrink=0.05))

# Show the chart
plt.show()
plt.savefig('png_files/plot_f238649b.png')