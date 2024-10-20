# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'Average Data Usage (GB)': [10.5, 8.2, 6.5, 5.1, 4.3, 3.8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Age Group'], df['Average Data Usage (GB)'])
plt.xlabel('Age Group')
plt.ylabel('Average Data Usage (GB)')
plt.title('Average Data Usage by Age Group')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()
plt.savefig('png_files/plot_9f3fe566.png')