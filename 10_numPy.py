# Creating an array:


import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

# Creating a 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3)


# Accessing elements in an array:

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing a single element
print(arr[0, 1])  # Output: 2

# Accessing a row
print(arr[1])  # Output: [4 5 6]

# Accessing a column
print(arr[:, 2])  # Output: [3 6 9]

# Accessing a sub-array
print(arr[0:2, 1:3])  # Output: [[2 3] [5 6]]


# Array manipulation:

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Reshaping an array
print(arr.reshape(9, 1))  # Output: [[1] [2] [3] [4] [5] [6] [7] [8] [9]]

# Flattening an array
print(arr.flatten())  # Output: [1 2 3 4 5 6 7 8 9]

# Transposing an array
print(arr.T)  # Output: [[1 4 7] [2 5 8] [3 6 9]]

# Concatenating arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2)))  # Output: [[1 2] [3 4] [5 6] [7 8]]


# Array operations:

arr = np.array([1, 2, 3, 4, 5])

# Summing an array
print(np.sum(arr))  # Output: 15

# Finding the maximum value in an array
print(np.max(arr))  # Output: 5

# Finding the minimum value in an array
print(np.min(arr))  # Output: 1

# Finding the mean of an array
print(np.mean(arr))  # Output: 3.00
