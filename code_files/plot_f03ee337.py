import pandas as pd

# Sample data
data = {
    'Device Model': ['iPhone 13', 'iPhone 13', 'iPhone 12', 'iPhone 12', 'Samsung S22', 'Samsung S22', 'Samsung S21', 'Samsung S21'],
    'Screen On Time (minutes)': [420, 450, 380, 400, 500, 520, 480, 500]
}

df = pd.DataFrame(data)
```

### Code

```
import matplotlib.pyplot as plt

# Group by device model and calculate average screen on time
average_screen_on_time = df.groupby('Device Model')['Screen On Time (minutes)'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_screen_on_time['Device Model'], average_screen_on_time['Screen On Time (minutes)'])
plt.xlabel('Device Model')
plt.ylabel('Average Screen On Time (minutes)')
plt.title('Average Screen On Time by Device Model')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_f03ee337.png')