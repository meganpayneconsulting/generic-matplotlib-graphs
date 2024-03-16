"""
Create a generic histogram with simulated data. 

Using the normal distribution with mean mu and standard deviation sigma^2.
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate data from a normal distribution
np.random.seed(42)
mu = 0
sigma2 = 1
num_samples = 1000
data = np.random.normal(mu, sigma2, num_samples)

# Create histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Title and suptitle
plt.suptitle('Histogram of Data from Normal Distribution')
plt.title(f'Mean = {mu}, Standard Deviation = {sigma2}')

# Axes labels
plt.xlabel('Value of Simulated Data')
plt.ylabel('Frequency of Simulatd Data')

# Turn on grid
plt.grid(True)

# Caption
plt.figtext(0.5, 0.01, 
            f'Data generated from a normal distribution with mean {mu} and standard deviation {sigma2}',
            ha='center', fontsize=10)

plt.show()