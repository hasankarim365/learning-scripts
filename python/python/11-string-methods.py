name = "john"

result = len(name) # length of str
print(result)

result = name.find("a") # Find first occurunce
print(result) # 1

result = name.rfind("a") # Find last occurunce
print(result) # 

name = name.capitalize() # Capitalizes the first letter of a string
print(name)

name = name.upper() # Capitalizes the whole string
print(name)

name = name.lower() # Makes the string all lowercase
print(name)

result = name.isdigit() #Checks if the string is made up of only int (No Spaces)
print(result) # False

result = name.isalpha()
print(result) # True

result = name.count() # Counts how many characters
print(result)

name = name.replase("a", "e")
print(name)

print(help(str)) # prints library of string methods
