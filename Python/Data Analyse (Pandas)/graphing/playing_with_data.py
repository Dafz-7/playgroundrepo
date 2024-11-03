import matplotlib.pyplot as plt
import numpy as np

# Data
midpoints = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])  # Midpoints of each interval
frequencies = np.array([2, 4, 8, 9, 12, 13, 8, 7, 6, 1])

# Calculate cumulative frequencies
cumulative_frequencies = np.cumsum(frequencies)

# Calculate the mean (weighted mean based on midpoints and frequencies)
mean = np.average(midpoints, weights=frequencies)

# Calculate the variance
variance = np.average((midpoints - mean)**2, weights=frequencies)

# Calculate the standard deviation
std_dev = np.sqrt(variance)

# Plot cumulative frequency graph
plt.figure(figsize=(8, 6))
plt.plot(midpoints, cumulative_frequencies, marker="o", linestyle="-", color="b", label="Cumulative Frequency")
plt.xlabel("Time (hours)")
plt.ylabel("Cumulative Frequency")
plt.title("Cumulative Frequency Diagram")
plt.grid(True)
plt.legend()

# Display the standard deviation on the plot
plt.text(50, max(cumulative_frequencies) - 5, f"Standard Deviation: {std_dev:.2f}", fontsize=12, color="red")

# Show the plot
plt.show()