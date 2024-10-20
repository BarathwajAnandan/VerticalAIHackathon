import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Operating System': ['Windows', 'macOS', 'Linux', 'Android', 'iOS'],
    'Number of Apps': [1000, 800, 600, 1200, 900]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Operating System'], df['Number of Apps'], color='skyblue')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')
plt.title('Number of Apps Installed by Operating System')
plt.xticks(rotation=45)

# Add labels to the bars
for i, value in enumerate(df['Number of Apps']):
    plt.text(i, value + 10, str(value), ha='center')

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_b4c9d13a.png')