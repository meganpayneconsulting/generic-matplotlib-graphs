"""
A generic horizontal barchart from simulated data.
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data using a seed for reproducibility
np.random.seed(42)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
data = np.random.randint(1, 100, size=len(categories))

# Create horizontal bar chart
plt.figure(figsize=(8, 6))
bars = plt.barh(categories, data, color='skyblue')

# Title and subtitle
plt.title('Horizontal Bar Chart of Randomly Generated Data')
plt.suptitle('Showing Random Data Distribution across Categories')

# Axes labels
plt.xlabel('Value of X data')
plt.ylabel('Categorues of data')

# Add data labels
for bar, value in zip(bars, data):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, str(value), va='center')

# Caption
plt.figtext(0.5, 0.01, 'Random data generated for demonstration purposes',
            ha='center', fontsize=10)

plt.show()
