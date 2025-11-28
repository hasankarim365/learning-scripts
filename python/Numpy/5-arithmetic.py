import numpy as np

array = np.array([1, 2, 3.2])

# Scalar arithmatic

print(array - 1) # Subtracts 1 from every element
print(array + 4) # Adds 4 to every element
print(array * 3) # Multiplies all elemnts by 3
print(array / 4) # Divides all elements by 4
print(array ** 5)# Prints every element to the power of 5

# Vectorised arithmetic

print(np.sqrt(array)) # Squares numbers
print(np.round(array)) # Rounds numbers
print(np.floor(array)) # Rounds numbers down
print(np.ceil(array)) # Rounds numbers up
print(np.pi) # Calls Constant Pi

# Element-wise arithmetic
# Applies operation between single elements between two or more arrays

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) 
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

# Prints a Boolean array that checks which element meets the requirements
print(scores == 100) # [False False  True False False False]
print(scores >= 60)
print(scores < 60)

# Conditional assignment

scores[scores < 60] = 0 # If there are scores less than 60, change them to 0
