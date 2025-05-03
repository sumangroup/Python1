import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print('arr: ',arr)
print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)
print("nbytes:", arr.nbytes)
print("transpose:\n", arr.T)

'''
| Attribute      | Description                            | Example (`arr`)           |
| -------------- | -------------------------------------- | ------------------------- |
| `arr.ndim`     | Number of dimensions                   | `2`                       |
| `arr.shape`    | Tuple of array dimensions (rows, cols) | `(2, 3)`                  |
| `arr.size`     | Total number of elements               | `6`                       |
| `arr.dtype`    | Data type of the elements              | `int64` (or `int32`)      |
| `arr.itemsize` | Size (in bytes) of each element        | `8` (for `int64`)         |
| `arr.nbytes`   | Total bytes consumed by the array      | `48` (6 elements × 8)     |
| `arr.T`        | Transpose of the array                 | Shape changes to `(3, 2)` |

'''
