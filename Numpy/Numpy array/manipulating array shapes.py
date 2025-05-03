import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print('arr',arr)
reshaped = arr.reshape((3,2))
print(reshaped)
print('-'*50)

arr2d = np.array([[1, 2], [3, 4]])
print(arr2d)
flat = arr2d.flatten()
print(flat)  # [1 2 3 4]
print('-'*50)

arr = np.array([[1, 2], [3, 4]])
print(arr)
transposed = arr.T
print(transposed)
print('-'*50)

arr = np.array([1, 2, 3, 4])
print(arr)
arr.resize((3, 3))
print(arr)
print('-'*50)

arr = np.array([1, 2, 3,5,6,7])
print(arr)
expanded = arr[:, np.newaxis]
print(expanded.shape)  # (3, 1)
print('-'*50)

arr = np.array([[[1, 2, 3]]])
print(arr)
squeezed = np.squeeze(arr)
print(squeezed.shape)  # (3,)








