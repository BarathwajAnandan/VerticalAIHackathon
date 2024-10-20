import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    'Operating System': ['Windows', 'Windows', 'Windows', 'Windows', 'Windows', 'MacOS', 'MacOS', 'MacOS', 'MacOS', 'Linux', 'Linux', 'Linux'],
    'Battery Drain (hours)': [2.5, 3.2, 2.8, 3.1, 2.9, 1.8, 2.1, 1.9, 2.3, 1.6, 1.7, 1.4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Operating System'] == 'Windows', 'Battery Drain (hours)'],
             df.loc[df['Operating System'] == 'MacOS', 'Battery Drain (hours)'],
             df.loc[df['Operating System'] == 'Linux', 'Battery Drain (hours)']],
            labels=['Windows', 'MacOS', 'Linux'],
            patch_artist=True)

# Set plot title and labels
plt.title('Battery Drain by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Battery Drain (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_6aa8b586.png')