# Line Plot: Plotting a line graph of a mathematical function.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Wave")
plt.show()


# Scatter Plot: Plotting a scatter plot of random data.


x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000*np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()


# Histogram: Plotting a histogram of a sample datasett

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.5)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")
plt.show()

# Bar Chart: Plotting a bar chart of a sample dataset.
x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([3, 5, 1, 7, 4])

plt.bar(x, y)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")
plt.show()


# Pie Chart: Plotting a pie chart of a sample dataset.
x = np.array([25, 40, 10, 25])
labels = ['A', 'B', 'C', 'D']

plt.pie(x, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
