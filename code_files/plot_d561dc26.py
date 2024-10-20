import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'age_group': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'data_usage': [10.2, 12.5, 9.8, 8.2, 6.5, 4.8]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(df['age_group'], df['data_usage'], color='#87CEEB')
plt.xlabel('Age Group')
plt.ylabel('Average Data Usage (GB)')
plt.title('Average Data Usage by Age Group')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_d561dc26.png')