import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr[0])
print(arr[-2])
print('-'*50)

arr2d=np.array([[10,20,30],[40,50,60]])
print(arr2d)
print(arr2d[1,2])
print('-'*50)

list1=[
    [10,20,30],
     [20,30,40] ]
print(list1[0][1])
print('-'*50)

print('Slicing')
#Slicing (Extracting Portions)
arr = np.array([10, 20, 30, 40, 50])
print(arr)
print(arr[1:4])
print(arr[1:])
print(arr[:3])
print('-'*50)

print('2d')
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[0:3, 1:2])


'''
| Expression      | Description                  |
| --------------- | ---------------------------- |
| `arr[i]`        | ith element (1D)             |
| `arr[i, j]`     | element at row i, col j (2D) |
| `arr[a:b]`      | slice from a to b-1 (1D)     |
| `arr[a:b, c:d]` | 2D slice of rows/cols        |
| `arr[:, j]`     | all rows, jth column         |
| `arr[i, :]`     | ith row, all columns         |

'''
