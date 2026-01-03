import numpy as np
lst = [1, 2, 3]
arr = np.array([1, 2, 3])
print(arr * 2)   # [2 4 6]

#numpy array
arr = np.array([10, 20, 30])
print(arr)

#check array dimension and shape
arr = np.array([[1, 2], [3, 4]])
print(arr.ndim)    # Dimension
print(arr.shape)   # Shape

#reshape(returns new array)
arr = np.array([1,2,3,4])
print(arr.reshape(2,2))

#slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])   # [20 30 40]

#broadcasting
arr = np.array([1, 2, 3])
print(arr + 10)   # [11 12 13]

arr = np.array([10, 20, 30])

print(arr.max())
print(arr.min())
print(arr.sum())
print(arr.mean())

#matrix multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a,b))
