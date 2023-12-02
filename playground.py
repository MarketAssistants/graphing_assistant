import matplotlib.pyplot as plt
import numpy as np

# Generate example data
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black', label='Data')

# Add analysis information using plt.text()
plt.text(1.5, 50, 'Mean: {:.2f}'.format(np.mean(data)), fontsize=12, color='red')
plt.text(1.5, 45, 'Median: {:.2f}'.format(np.median(data)), fontsize=12, color='green')
plt.text(1.5, 40, 'Std Dev: {:.2f}'.format(np.std(data)), fontsize=12, color='purple')

# Add labels and legend
plt.title('Histogram with Analysis Information')
plt.xlabel('X-axis label')
plt.ylabel('Frequency')
plt.legend()

# Show the plot
plt.show()
