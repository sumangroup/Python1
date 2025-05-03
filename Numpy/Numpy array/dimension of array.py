import numpy as np

arr1 = np.array([1, 2, 3])            # 1D array
arr2 = np.array([[1, 2], [3, 4]])     # 2D array
arr3 = np.array(
    [
        [[1], [2]
         ],
     [
         [3], [4]]
        ]
    )  # 3D array

print(arr1.ndim)  # Output: 1
print(arr2.ndim)  # Output: 2
print(arr3.ndim)  # Output: 3


print(arr2.shape)  # (2, 2)
print(arr3.size)   # 4

'''
| Array | Example Input              | Dimensions (`ndim`) | Shape       |
| ----- | -------------------------- | ------------------- | ----------- |
| 1D    | `[1, 2, 3]`                | 1                   | `(3,)`      |
| 2D    | `[[1, 2], [3, 4]]`         | 2                   | `(2, 2)`    |
| 3D    | `[[[1], [2]], [[3], [4]]]` | 3                   | `(2, 2, 1)` |

'''
