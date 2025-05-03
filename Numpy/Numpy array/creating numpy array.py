import numpy as np
# From a list
array1=np.array([10,20,30])
print('array1',array1,len(array1))
print('-'*50)

# from 2d list
array2=np.array([[10,20],[40,60]])
print(array2,len(array2))
print('-'*50)

# Create an array of zeros
zeros = np.zeros((2, 3))  # 2 rows, 3 columns
print('zeros',zeros)
print('-'*50)

# Create an array of ones
ones = np.ones((3, 2))
print('ones',ones)
print('-'*50)

# Create a range of values
range_array = np.arange(0, 10,3)  # [0, 2, 4, 6, 8]
print('range_array',range_array)
print('-'*50)

# Create evenly spaced values
linspace_array = np.linspace(0, 5, 6)  # [0. 0.25 0.5 0.75 1.]
print('linspace_array',linspace_array)
print('-'*50)

identity = np.eye(3)
print('identity',identity)
print('-'*50)

random_array = np.random.rand(2, 5)
print('random_array',random_array)
print('-'*50)

# Random integers
randint_array = np.random.randint(0, 15, size=(3, 4))
print('randint_array',randint_array)
print('-'*50)
