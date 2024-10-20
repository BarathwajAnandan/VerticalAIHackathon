import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
data = {
    'Operating System': np.repeat(['Android', 'iOS', 'Windows'], 100),
    'App Usage Time (minutes)': np.random.randint(1, 100, 300)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([df.loc[df['Operating System'] == 'Android', 'App Usage Time (minutes)'],
             df.loc[df['Operating System'] == 'iOS', 'App Usage Time (minutes)'],
             df.loc[df['Operating System'] == 'Windows', 'App Usage Time (minutes)']],
            labels=['Android', 'iOS', 'Windows'])
plt.title('Box Plot of App Usage Time by Operating System')
plt.xlabel('Operating System')
plt.ylabel('App Usage Time (minutes)')
plt.show()
plt.savefig('png_files/plot_0f484984.png')