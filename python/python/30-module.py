print(help("modules")) # shows list of different modules
print(help("math")) # Import math

import math as m # now each time you call math you use m
print(m.pi)

from math import pi
print(pi) # this may cause variable name conflicts

# To create a module, create a new python file within the same folder as your original file, create your varibles and functions, then in your original python file, import the new files name, now you can access the everything in the new tab