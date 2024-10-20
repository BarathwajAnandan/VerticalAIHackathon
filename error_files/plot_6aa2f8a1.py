# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Screen On Time (minutes)': [120, 150, 180, 200, 220, 90, 110, 130, 140, 160,
                                 180, 200, 220, 240, 260, 90, 110, 130, 140, 160]
}
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'].values,
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)'].values],
            labels=['Male', 'Female'])
plt.title('Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')
plt.show()
```

This code will create a box plot with two boxes, one for males and one for females, showing the distribution of screen on time for each gender.

Please note that you need to have `pandas` and `matplotlib` installed in your  environment to run this code. You can install them using pip:

```bash
pip install pandas matplotlib
plt.savefig('png_files/plot_6aa2f8a1.png')