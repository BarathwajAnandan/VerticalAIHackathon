import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Operating System': ['Windows', 'MacOS', 'Linux', 'Windows', 'MacOS', 'Linux', 'Windows', 'MacOS', 'Linux'],
    'Number of Apps': [100, 50, 75, 120, 60, 90, 110, 55, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Operating System' and count the number of apps
grouped_df = df.groupby('Operating System')['Number of Apps'].sum().reset_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(grouped_df['Operating System'], grouped_df['Number of Apps'], color=['blue', 'green', 'red'])
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')
plt.title('Number of Apps Installed by Operating System')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_5dfbe6b4.png')