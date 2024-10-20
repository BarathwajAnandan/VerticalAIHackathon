bash
pip install matplotlib pandas
```
### Step 2: Sample Data

Create a sample dataset with device model information:
```
import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone 13', 'Samsung Galaxy S22', 'iPhone 13', 'Google Pixel 6', 'Samsung Galaxy S22', 'iPhone 13', 'Google Pixel 6', 'Samsung Galaxy S22', 'iPhone 13'],
    'Count': [3, 2, 2, 1, 2, 2, 1, 2, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)
```
### Step 3: Create a Pie Chart

Now, create a pie chart using `matplotlib`:
```
import matplotlib.pyplot as plt

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(df['Count'], labels=df['Device Model'], autopct='%1.1f%%')
plt.title('Device Model Distribution')
plt.show()
plt.savefig('png_files/plot_1d0e0e04.png')