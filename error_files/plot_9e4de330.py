# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Operating System': np.random.choice(['Windows', 'MacOS', 'Linux'], 100),
    'Battery Drain (mAh)': np.random.uniform(0, 100, 100)
}
df = pd.DataFrame(data)

# Group the data by operating system and calculate the battery drain
grouped_df = df.groupby('Operating System')['Battery Drain (mAh)'].describe()

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot([grouped_df['Battery Drain (mAh)'].loc['Windows'],
             grouped_df['Battery Drain (mAh)'].loc['MacOS'],
             grouped_df['Battery Drain (mAh)'].loc['Linux']],
            labels=['Windows', 'MacOS', 'Linux'],
            vert=False)
plt.title('Box Plot of Battery Drain by Operating System')
plt.xlabel('Battery Drain (mAh)')
plt.ylabel('Operating System')
plt.show()
plt.savefig('png_files/plot_9e4de330.png')