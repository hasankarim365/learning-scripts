import numpy as np

array = np.array([ ["1","2","3","4"],
                   ["5","6","7","8"],
                   ["9","10","11","12"],
                   ["13","14","15","16"] ])
print(array[0, 0]) # [row, column]. This selects row index 0 and column index 0

print(array[ :, 0]) # [ : , 0]. This selects all rows and column index 0
print(array[ :, 0:3]) # Slicing the columns. Prints columns 0 - 2
print(array[:, ::2]) # Prints the first, skips the second, prints the third

print(array[0:2, :0:3]) # Slicing both the row and columns
print(array[2:0, 0:2])