import numpy as np

#Broadcasting allows Numpy to perform operations on arrays with different shapes by virtually expanding dimension so the match the  larger arrays shape
#In order for broadcasting to work, the dimensions of the arrays must be the same size, or have a dimension od size one

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)