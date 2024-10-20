import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'Average Data Usage (GB)': [10.2, 12.5, 15.1, 11.8, 9.5, 7.2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Average Data Usage (GB)'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Average Data Usage (GB)')
plt.title('Average Data Usage by Age Group')
plt.xticks(rotation=45)

# Add data labels
for i, value in enumerate(df['Average Data Usage (GB)']):
    plt.text(i, value + 0.5, str(value), ha='center')

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_2884c80c.png')