import numpy as np

v = np.array([3,2])

B1 = np.array([[1,0],[0,1]])

B2 = np.array([[1,1],[1,-1]])

B3 = np.array([[2,1],[1,2]])

print(np.linalg.inv(B1)@v)
print(np.linalg.inv(B2)@v)
print(np.linalg.inv(B3)@v)