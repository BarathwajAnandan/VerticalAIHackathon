import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55-64'],
    'Average App Usage Time': [2.5, 3.2, 2.8, 2.1, 1.9]
}
df = pd.DataFrame(data)

# Create a line plot
plt.figure(figsize=(8, 6))
plt.plot(df['Age Group'], df['Average App Usage Time'], marker='o')

# Set title and labels
plt.title('Average App Usage Time by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average App Usage Time (hours)')

# Show the plot
plt.show()
plt.savefig('png_files/plot_382548f4.png')