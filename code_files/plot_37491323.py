import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data
data = {
    'Number of Apps Installed': np.random.randint(1, 100, 100),
    'Data Usage (MB)': np.random.randint(100, 10000, 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Number of Apps Installed'], df['Data Usage (MB)'])

# Set title and labels
plt.title('Scatter Plot of Number of Apps Installed vs. Data Usage')
plt.xlabel('Number of Apps Installed')
plt.ylabel('Data Usage (MB)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_37491323.png')