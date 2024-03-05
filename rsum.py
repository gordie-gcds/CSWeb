import numpy as np

import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return x**2

# Define the limits of integration
a = 0
b = 5

# Define the number of subintervals
n = 100

# Calculate the width of each subinterval
dx = (b - a) / n

# Generate the x-values for the subintervals
x = np.linspace(a, b, n+1)

# Calculate the y-values for the function
y = f(x)

# Calculate the Riemann sum
riemann_sum = np.sum(y[:-1] * dx)

# Plot the function
plt.plot(x, y, 'b-', linewidth=2)

# Plot the rectangles for the Riemann sum
for i in range(n):
    plt.fill_between([x[i], x[i+1]], [0, 0], [y[i], y[i]], color='red', alpha=0.5)

# Set the x and y axis labels
plt.xlabel('x')
plt.ylabel('f(x)')

# Set the title of the plot
plt.title('Riemann Sum')

# Show the Riemann sum value on the plot
plt.text(0.5 * (a + b), 0.5 * np.max(y), f'Riemann Sum = {riemann_sum}', ha='center', va='center')

# Display the plot
plt.show()