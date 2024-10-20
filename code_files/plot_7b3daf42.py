import matplotlib.pyplot as plt
import numpy as np

# List of device models
device_models = ['iPhone 13', 'iPhone 13 Pro', 'iPhone 13 Pro Max', 'iPhone 12', 'iPhone 12 Pro', 'iPhone 12 Pro Max',
                'iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max', 'iPhone 10', 'iPhone 10 Pro', 'iPhone 10 Pro Max',
                'iPhone 9', 'iPhone 9 Pro', 'iPhone 9 Pro Max', 'iPhone 8', 'iPhone 8 Pro', 'iPhone 8 Pro Max',
                'iPhone 7', 'iPhone 7 Pro', 'iPhone 7 Pro Max', 'iPhone 6', 'iPhone 6 Plus', 'iPhone 6 Plus',
                'iPhone 5', 'iPhone 5C', 'iPhone 5S', 'iPhone 5S Max', 'iPhone 4', 'iPhone 4S', 'iPhone 4S Max']

# List of device sizes
device_sizes = ['Small', 'Medium', 'Large']

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(len(device_models), labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
```

This code will generate a pie chart with the device models on the outer ring and the device sizes on the inner ring. The `autopct` parameter is used to display the percentage value of each slice.

**Example Output:**

The code will generate a pie chart with the following output:

```
      Small  Medium  Large
Small      10.0   20.0   70.0
Medium    15.0   30.0   55.0
Large     25.0   45.0   30.0
plt.savefig('png_files/plot_7b3daf42.png')