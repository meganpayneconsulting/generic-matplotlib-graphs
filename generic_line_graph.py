"""
Generic line graphs
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate sample data, using seed for reproducibility
np.random.seed(42)
num_points = 12
dates = pd.date_range('2023-01-01', periods=num_points)
weeks = np.arange(1, num_points + 1)
data1 = np.random.randint(1, 100, size=num_points)
data2 = np.random.randint(1, 100, size=num_points)

# Create line chart with dates on x-axis
plt.figure(figsize=(10, 6))
plt.plot(dates, data1, marker='o', linestyle='-', color='blue', label='Data 1')
plt.plot(dates, data2, marker='s', linestyle='--', color='green', label='Data 2')

# Title and subtitle 
plt.title('Line Graph Using Simulated Data By Date')
plt.suptitle('Comparison of Data 1 and Data 2')

# Axes labels
plt.xlabel('Date of Fake Action')
plt.ylabel('Value of Fake Action')

# Legend
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()

# Create line chart with weeks on x-axis
plt.figure(figsize=(10, 6))
plt.plot(weeks, data1, marker='o', linestyle='-', color='blue', label='Data 1')
plt.plot(weeks, data2, marker='s', linestyle='--', color='green', label='Data 2')

# Title and subtitle
plt.title('Line Chart By Week on X-Axis')
plt.suptitle('Comparison of Data 1 and Data 2')

# Axes labels
plt.xlabel('Week Number')
plt.ylabel('Value of Fake Data')

# Legend
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()
