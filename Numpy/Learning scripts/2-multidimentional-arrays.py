import numpy as np

array = np.array("A") # This is a zero-dimentional array
print(array.ndim) # Shows us the number of dimentions in an array

array = np.array(["A","B","C"]) # This is a one-dimentional array
print(array.ndim)

array = np.array(["A","B","C"]) # This is a one-dimentional array
print(array.ndim)

array = np.array([["A","B","C"],
                  ["1","2","3"],
                  ["H","A","K"]]) # This is a two-dimentional array. The one-dimensional array is nested in another list
print(array.ndim)

array = np.array([[["A","B","C"],["1","2","3"],["H","A","K"]],
                  [["A","B","C"],["1","2","3"],["H","A","K"]],
                  [["A","B","C"],["1","2","3"],["H","A","K"]]]) # This is a three-dimentional array. The two-dimensional array is nested in another list
                  # Each of the list need to have a consitant number of elements
print(array.ndim)
#This goes up to 5 dimensions

print(array.shape)# This shows the shape of the array. It returns a tuple of integers (layers, rows, columns)

print(array[0,0,0]) # This is called multidimentonal indexing. [layers, rows, columns]. This is faster then chain indexing 

word = array[0,0,0] + array[0,1,0] + array[0,2,2]
print(type(word)) # Outputs it as a numpy.str

