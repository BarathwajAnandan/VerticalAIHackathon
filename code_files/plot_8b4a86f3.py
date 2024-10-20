import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Operating System': ['Windows', 'Windows', 'Windows', 'MacOS', 'MacOS', 'MacOS', 'Linux', 'Linux', 'Linux'],
    'Screen On Time (minutes)': [120, 150, 180, 100, 120, 150, 80, 100, 120]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate average screen on time for each operating system
average_screen_on_time = df.groupby('Operating System')['Screen On Time (minutes)'].mean()

# Create a bar chart
plt.figure(figsize=(10, 6))
average_screen_on_time.plot(kind='bar')
plt.title('Average Screen On Time by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Average Screen On Time (minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_8b4a86f3.png')