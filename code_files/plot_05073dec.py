# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'User_Behavior_Class': ['Gaming', 'Video Streaming', 'Social Media', 'Music Streaming', 'Browsing'],
    'Average_Battery_Drain': [25, 20, 15, 10, 5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10,6))
plt.bar(df['User_Behavior_Class'], df['Average_Battery_Drain'], color='skyblue')
plt.xlabel('User Behavior Class')
plt.ylabel('Average Battery Drain (%)')
plt.title('Bar Plot of Average Battery Drain by User Behavior Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_05073dec.png')