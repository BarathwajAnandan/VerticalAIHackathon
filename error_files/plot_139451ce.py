import matplotlib.pyplot as plt
import numpy as np

# Data
operating_systems = ['Windows', 'MacOS', 'Android', 'iOS']
num_apps = [1000, 500, 2000, 1500]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(operating_systems, num_apps, color='skyblue')

# Set title and labels
plt.title('Number of Apps Installed by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')

# Add a legend
plt.legend(labels=operating_systems, loc='upper right')

# Show the plot
plt.show()
```

This code will create a bar plot with the operating systems on the x-axis and the number of apps installed on the y-axis. Each operating system is represented by a different color.

If you want to save the plot to a file, you can use the `savefig` method:

```
plt.savefig('app_installation_by_os.png')
```

This will save the plot as a PNG file named `app_installation_by_os.png` in the current working directory.

You can also use the `seaborn` library to create a more visually appealing plot:

```
import seaborn as sns
import matplotlib.pyplot as plt

# Data
operating_systems = ['Windows', 'MacOS', 'Android', 'iOS']
num_apps = [1000, 500, 2000, 1500]

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=operating_systems, y=num_apps, color='skyblue')

# Set title and labels
plt.title('Number of Apps Installed by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Number of Apps')

# Show the plot
plt.show()
plt.savefig('png_files/plot_139451ce.png')