#create a 1D array of numbers from 0 - 9
import numpy as np
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array[0:10])

#create a 3 x 3 NumPy array of all boolean values True
print (np.ones((3, 3), dtype=bool))

#Extract all the odd numbers from an array of 1-10
import numpy as np
array = np.arange(1,10,2)
print(array)

#Replace all odd numbers in an array of 1-10 with the value -1
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
odd_values = (a%2 ==1)
a[odd_values] = -1
print(a)

#Convert a 1d array to a 2d array with 2 rows
import numpy as np
array = np.arange(6).reshape(2,3)
print(array)

#create two arrays a and b, stack these 2 arrays vertically use the np.dot and np.sum to calculate totals
import numpy as np
array_a = np.array([1, 2, 3, 4])
array_b = np.array([5, 6, 7, 8])
arr = np.dstack((array_a, array_b))
print(arr)
c = np.dot(array_a, array_b)
print(c)
sum = np.sum(c)
print(sum)

#create th efollowing pattern without nhardcording, Use only numPy functions.>array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,123])
import numpy as np
array = np.arange(1, 19, 1)
print(array)

























