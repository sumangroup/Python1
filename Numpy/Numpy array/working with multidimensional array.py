import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
print(arr2d[1,1])
print(arr2d[:,0:2])
print('-'*50)


# 3D Array (Matrix of Matrices)
arr3d = np.array([
    [
        [1, 2],
        [3, 4]
     ],
    
    [
        [5, 6],
        [7, 8]
        ]
])
print(arr3d)
print(arr3d[1,1,1])
print(arr3d[1,0:1,0:2])

print('operation of element-wise')
print(arr2d + 10)     # Add 10 to every element
print(np.sum(arr2d))  # Sum of all elements
print(arr3d.T)        # Transpose
