import numpy as np

X = np.array([
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 2],
    [1, 3, 4],
    [1, 5, 3],
    [1, 6, 2]
])

y = np.array([1, 1, 1, -1, -1, -1]).T

w = np.linalg.lstsq(X, y)[0]

print(w)

import matplotlib.pyplot as plt  

plt.scatter(X[:,1], X[:,2])