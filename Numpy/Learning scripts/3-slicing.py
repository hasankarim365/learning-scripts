import numpy as np

array = np.array([ ["1","2","3","4"],
                   ["5","6","7","8"],
                   ["9","10","11","12"],
                   ["13","14","15","16"] ])

print(array[-1]) # This is negative indexing. This one prints the last row

#print(array[start(inclusive):stop(inclusive):step]) # This is a slicing expression.
print(array[0:3])
print(array[-3:4]) # This starts from the 3rd last row
print(array[0:]) # Having a blank stop means to use all layers

print(array[::2]) # Prints row one, skips row two, prints row three, ...
print(array[::-1]) # Prints array backwards
print(array[::-2]) # Prints row four, skips row three, prints row two, ...