import numpy as np
from matplotlib import pyplot as plt

x = np.array([0.5, 1, 2, 2, 2, 3.5, 3.75, 4.25])
y = x**3

plt.scatter(x, y)
plt.plot(x, y)

plt.show()
