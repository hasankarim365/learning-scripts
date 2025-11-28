import numpy as np

array = np.array([[1,2,3,4,5], 
                  [6,7,8,9,10]])

# Boolean Indexing

num = array[array < 5] # Creates a list of values that are in array that are smaller than 5
print(num)

num = array[(array <= 7) & (array > 2)] # Creates a list of values that are in array that are smaller than or equal to  7 and(&) bigger than 2
print(num)

num = array[(array < 3) | (array > 7)] # Creates a list of values that are in array that are smaller than 3 or(|) bigger than 7
print(num)

evens = array[array % 2 == 0]# Creates a list of values that are in array that when divided by 2 have a remainder of 0
print(evens)

# Where function

evens = np.where(array % 2 == 0, array, 0) # The where function conserves the shape of the array by substituting number that don't match the requirements with something else. 
#(array, 0) is saying that any number that don't match the requirements, will be substituted with 0 
print(evens)

evens = np.where(array % 2 == 0, array, -100)
print(evens) # This is slower than boolean indexing, but conserves the shape of the list

