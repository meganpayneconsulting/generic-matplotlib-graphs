"""
This is a generic scatterplot created with generated data. 
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate data using seed for reproducibility
np.random.seed(42)
mean1, std1 = 10, 2
mean2, std2 = 20, 3
mean3, std3 = 15, 4
num_points = 100
x1 = np.random.normal(mean1, std1, num_points)
y1 = np.random.normal(mean1, std1, num_points)
x2 = np.random.normal(mean2, std2, num_points)
y2 = np.random.normal(mean2, std2, num_points)
x3 = np.random.normal(mean3, std3, num_points)
y3 = np.random.normal(mean3, std3, num_points)

# Create scatterplot of different groups
plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='green', label='Group 2')
plt.scatter(x3, y3, color='red', label='Group 3')

# Title and subtitle
plt.title('Scatterplot of Synthetic Data')
plt.suptitle('Data Generated from 3 Normal Distributions')

# Axes labels
plt.xlabel('X-axis Label of Data')
plt.ylabel('Y-axis Label of Data')

# Legend
plt.legend()

# Caption
plt.figtext(0.5, 0.01, 'Data points generated from normal distributions with different means and standard deviations',
            ha='center', fontsize=10)

plt.show()
