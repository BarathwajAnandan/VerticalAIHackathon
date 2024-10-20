import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
data = {
    'User Behavior Class': np.random.choice(['Class A', 'Class B', 'Class C'], size=100),
    'Battery Drain': np.random.uniform(0, 100, size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the average battery drain by user behavior class
average_battery_drain = df.groupby('User Behavior Class')['Battery Drain'].mean().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(average_battery_drain['User Behavior Class'], average_battery_drain['Battery Drain'], color='skyblue')
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain')
plt.title('Average Battery Drain by User Behavior Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_922b92b4.png')