import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
np.random.seed(0)
data = {
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Screen On Time (minutes)': np.random.randint(30, 120, 100)
}

df = pd.DataFrame(data)

# Create box plot
plt.figure(figsize=(8, 6))
plt.boxplot([df.loc[df['Gender'] == 'Male', 'Screen On Time (minutes)'], 
             df.loc[df['Gender'] == 'Female', 'Screen On Time (minutes)']],
            labels=['Male', 'Female'], patch_artist=True)

# Set plot properties
plt.title('Box Plot of Screen On Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen On Time (minutes)')
plt.show()
plt.savefig('png_files/plot_9164a031.png')