fruits = ["Apples", "Bananas", "Orange"] # List
print(fruits[2]) # Print fruits index 2 / Orange

# print(dir(fruits))
# print(help(fruits)) # list methods

print("Apple" in fruits) # Returns True

fruits[0] = "Pinapple"
fruits.append("pinapple")
fruits.remove("apple")
fruits.insert(0, "Pinapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("Bananas"))

fruits = {"Apples", "Bananas", "Orange", "Orange"} # Set
print(fruits) # unordered and gets rid of duplicates
print(dir(fruits))
print(help(fruits)) # set methods
print(len(fruits))
print("Apple" in fruits) # Returns True

fruits = ("Apples", "Bananas", "Orange") # Tuple
print(fruits) # ordered and unchangeable
print(dir(fruits))
print(help(fruits)) # list methods
print("Apple" in fruits) # Returns True
print(len(fruits))
print(fruits.index("apple"))
print(fruits.count("Bananas"))
