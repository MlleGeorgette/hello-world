"""
This tutorial shows the difference between a list and an array.
A list is useful for storing simple data where no mathematical calculation is expected.
However, arrays are more efficient for storing large datasets and for performing calculations.
Sources:
https://learnpython.com/blog/python-array-vs-list/
https://www.youtube.com/watch?v=mOZ0UCeuRX4
"""
import array as arr
import numpy as np

# Array using array module
array_1 = arr.array("i", [2, 4, 6, 8]) # "i" means all items in the array are integers
print(array_1)
print(type(array_1))

# Array using numpy module. Numpy arrays can have elements of different data type
array_2 = np.array(["string", 2, 4, 6, 8])
print(array_2)
print(type(array_2))

# Division using a numpy array
array_3 = np.array([10, 20, 30, 40])
division = array_3/2
print(division)
print(type(division))

# Cf the above with Python's built-in lists. No need to declare the data structure as a list
list_1 = [2, 4, 6, 8]
print(list_1)
print(type(list_1))

# Much less efficient to do a division with a list
division = []
for i in range(len(list_1)):
    result = list_1[i]/2
    division.append(result)
print(division)
print(type(division))

# Creating an empty array
empty_array1 = np.empty(4)
print(empty_array1)

empty_array2 = np.empty([3, 3])
print(empty_array2)

zero_array = np.zeros(4)
print(zero_array)
