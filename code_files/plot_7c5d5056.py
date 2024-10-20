import matplotlib.pyplot as plt

# Define the data
device_models = ['iPhone 14', 'Samsung S22', 'Google Pixel 6', 'OnePlus 9', 'Other', 'Huawei P30']
num_devices = [250, 200, 150, 100, 100, 50]

# Create a pie chart
plt.pie(num_devices, labels=device_models, autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
```

This code will generate a pie chart with the device models on the labels and the percentage of each device model displayed on the chart.

If you want to create a pie chart using Excel or Google Sheets, you can follow these steps:

1. Enter the data into a table with two columns: Device Model and Number of Devices.
2. Select the data range.
3. Go to the "Insert" tab and click on "Pie Chart".
4. Choose the type of pie chart you want to create (e.g. 2D or 3D).
5. Customize the chart as needed (e.g. add title, labels, etc.).

Here is a more complex example using , matplotlib and pandas.

```
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Device Model': ['iPhone 14', 'Samsung S22', 'Google Pixel 6', 'OnePlus 9', 'Other', 'Huawei P30'],
    'Number of Devices': [250, 200, 150, 100, 100, 50]
}
df = pd.DataFrame(data)

# Create a pie chart
plt.figure(figsize=(10,8))
plt.pie(df['Number of Devices'], labels=df['Device Model'], autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
```

And here is the same example but using plotly.

```
import plotly.express as px
import pandas as pd

# Create a DataFrame
data = {
    'Device Model': ['iPhone 14', 'Samsung S22', 'Google Pixel 6', 'OnePlus 9', 'Other', 'Huawei P30'],
    'Number of Devices': [250, 200, 150, 100, 100, 50]
}
df = pd.DataFrame(data)

# Create a pie chart
fig = px.pie(df, values='Number of Devices', names='Device Model')
fig.update_layout(title_text='Device Model Distribution')
fig.show()
plt.savefig('png_files/plot_7c5d5056.png')