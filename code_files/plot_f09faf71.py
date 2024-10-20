import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    "Operating System": ["Windows", "Windows", "Windows", "Linux", "Linux", "Linux", "MacOS", "MacOS", "MacOS"],
    "Count": [3, 2, 1, 4, 3, 2, 3, 2, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(df["Count"], labels=df["Operating System"], autopct='%1.1f%%')
plt.title("Operating System Distribution")
plt.show()
plt.savefig('png_files/plot_f09faf71.png')