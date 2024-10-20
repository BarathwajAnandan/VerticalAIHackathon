# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data
user_behavior = {
    'User A': {'login_time': 10, 'logout_time': 5, 'avg_battery_drain': 0.5},
    'User B': {'login_time': 15, 'logout_time': 10, 'avg_battery_drain': 0.7},
    'User C': {'login_time': 20, 'logout_time': 15, 'avg_battery_drain': 0.3},
    'User D': {'login_time': 25, 'logout_time': 20, 'avg_battery_drain': 0.9},
    'User E': {'login_time': 30, 'logout_time': 25, 'avg_battery_drain': 0.6},
}

# Calculate average battery drain for each user
user_avg_battery_drain = {}
for user, data in user_behavior.items():
    avg_battery_drain = np.mean([data['login_time'], data['logout_time']])
    user_avg_battery_drain[user] = avg_battery_drain

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(user_avg_battery_drain.keys(), user_avg_battery_drain.values())
plt.xlabel('User Behavior')
plt.ylabel('Average Battery Drain')
plt.title('Average Battery Drain by User Behavior')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
plt.savefig('png_files/plot_7b643111.png')