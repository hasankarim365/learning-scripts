#                   Number 1 (print)

# print("Hello World")

#                   Number 2 (Variables)

# first_name = "John"
# last_name = "Doe"
# Exam_score = 98.2
# is_student = True

# print(f"I am {first_name} {last_name}, I got {Exam_score}% on my exam")
# print(f"My name is John Doe: {is_student}")


#                   Number 3 (If statements)


# Balance = 50

# if Balance == 50:
#     print(f"You have £{Balance}")
# elif Balance > 50:
#     print(f"You have more than £{Balance}")
# else:
#     print(f"You don't have £{Balance}")


#                   Number 4 (Casting)


# string = "True"
# num = "26"
# num = int(num)
# deci = float(num)
# boolean = bool(str)
# string = str(boolean)

# print(string, num, deci, boolean)
# print(type(deci))


#                   Number 5 (Input)


# input("What is your name? ")
# age = int(input("What is your age? "))
# print(f"Your age is {age}")


#                   Number 6 (Arithmetic)


# num = 0
# num += 1 # simplified from num = num + 1
# print(num) #1

# num -= 2 # simplified from num = num - 2
# print(num) #-1

# num *= 3 # simplified from num = num * 3
# print(num) #-3

# num **= 2 # simplified from num = num ** 2
# print(num) # 6

# num = num % 2 # remainder or MOD
# print(num) # 0


#                   Number 7 (Maths functions)


# x = 3.14
# y = -4
# z = 5

# result = round(x) # rounds the number
# print(result) # 3

# result = abs(y) #absolute value
# print(result) # 4

# result = pow(y, 3)
# print(result) #-64

# result = max(x, y, z)
# print(max) # 5

# result = min(x, y, z)
# print(result) # -4


#                   Number 8 (Import maths)

# import math

# print(math.pi)
# print(math.e)

# result = math.sqrt(64)
# print(result) # 8

# result = math.ceil(9.1) # rounds up
# print(result) # 10

# result = math.floor(9.9)
# print(result) # 9


#                   Number 9 (Logical Operators)


# temp = 30
# is_sunny = True

# if temp == 30 and not is_sunny:   # "and", "or" and "not" is a Logic operator
#     print("It is hot and cloudy outside")
# elif is_sunny:
#     print("It is sunny")


#                   Number 10 (Conditional Expressions)


# num = 6
# print("Positive" if num > 0 else "Negative") # Positive

# num = -4
# result = "Positive" if num > 0 else "Negative"
# print(result) # Negative


#                   Number 11 (String Methods)


# name = "john"

# result = len(name) # length of str
# print(result)

# result = name.find("a") # Find first occurunce
# print(result) # 1

# result = name.rfind("a") # Find last occurunce
# print(result) # 

# name = name.capitalize() # Capitalizes the first letter of a string
# print(name)

# name = name.upper() # Capitalizes the whole string
# print(name)

# name = name.lower() # Makes the string all lowercase
# print(name)

# result = name.isdigit() #Checks if the string is made up of only int (No Spaces)
# print(result) # False

# result = name.isalpha()
# print(result) # True

# result = name.count() # Counts how many characters
# print(result)

# name = name.replase("a", "e")
# print(name)

# print(help(str)) # prints library of string methods


#                   Number 12 (Indexing)


# credit_number = "1234_5678_9012"
# print(credit_number[0:5:2]) # [start:stop:end]


#                   Number 13 (Format specifiers)


# :.numberf = round to number dp
# :number = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator


#                   Number 14 (While Loops)


# age = input("What is your age: ")

# while not age.isdigit(): # loops if age does not consist of only numbers
#     print("Enter only number")
#     age = input("What is your age: ")


#                   Number 15 (For loops)


# for x in range(1, 11): #(Inclusive, Exclusive)
#     print(x)

# for x in reversed(range(1,11, 2)): #(count down from 10, steps of 2)
#     print(x)


#                   Number 16 (Import time)


# import time

# my_time = int(input("Enter time in seconds: "))

# for x in reversed(range(0, my_time)):
#     print(x)
#     time.sleep(1) # Between each iteration delay for 1 second


#                   Number 17 (Nested Loop)


# for x in range(3):
#     for y in range(1,11):
#         print(y, end="")


#                   Number 18 (Collections)


# fruits = ["Apples", "Bananas", "Orange"] # List
# print(fruits[2]) # Print fruits index 2 / Orange

# print(dir(fruits))
# print(help(fruits)) # list methods

# print("Apple" in fruits) # Returns True

# fruits[0] = "Pinapple"
# fruits.append("pinapple")
# fruits.remove("apple")
# fruits.insert(0, "Pinapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("Bananas"))

# fruits = {"Apples", "Bananas", "Orange", "Orange"} # Set
# print(fruits) # unordered and gets rid of duplicates
# print(dir(fruits))
# print(help(fruits)) # set methods
# print(len(fruits))
# print("Apple" in fruits) # Returns True

# fruits = ("Apples", "Bananas", "Orange") # Tuple
# print(fruits) # ordered and unchangeable
# print(dir(fruits))
# print(help(fruits)) # list methods
# print("Apple" in fruits) # Returns True
# print(len(fruits))
# print(fruits.index("apple"))
# print(fruits.count("Bananas"))


#                   Number 19 (2D Collections)


# fruits = ["apple", "orange", "banana"]
# vegetables = ["celery", "carrots", "potatoes"]

# groceries = [fruits, vegetables]
# print(groceries)
# print(groceries[0][1]) # orange

# groceries = ["apple", "orange", "banana"], ["celery", "carrots", "potatoes"]
# print(groceries)
# print(groceries[0][1]) # orange


# for x in groceries:
#     for food in x:
#         print(food) # prints each member of the list individually


#                   Number 20 (Dictionaries)


# capitals = {
#     "USA": "Washington D.C.", 
#     "India": "New Delhi",
#     "China": "Beijing",
#     "Russia": "Moscow"
#     }

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# capitals.update({"Germany": "Berlin"})
# print(capitals)

# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# print(keys)

# values = capitals.values()
# print(values)

# for key, value in capitals.items():
#     print(f"{key}: {value}")


#                   Number 21 (Import Random)


# import random

# print(help(random)) # shows all methods

# number = random.randint(1, 10) # random int
# print(number)

# number = random.random() # Random float
# print(number)

# workers = ("Sam", "Mark", "Paul")
# cleaning_duty = random.choice(workers)
# print(cleaning_duty)

# ordered_list = [1,2,3,4,5,6,7,8,9]
# unordered_list = random.shuffle(ordered_list)
# print(unordered_list)


#                   Number 22 (Functions)


# def multiply(x, y): # takes parenthesis from the user
#     return x * y # returns x multiplies by y

# multiply(3, 29) # x, y
# multiply(int(input("Enter a number"), int(input("Enter a number")))) # x, y


#                   Number 23 (default arguments)


# def balance(cost, balance = 50): # balance is a default variable
#     wallet =  f"${balance - cost}"
#     if wallet < 0:
#         return "You can not afford this"
#     else:
#         return wallet

# cost = float(input("How much is the item? "))
# balance(cost) # 1 variable as balance is a default argument
# balance(cost, 60) # Uses 60 rather than 50


#                   Number 24 (keyword arguments)


# def balance(cost, balance = 50): # balance is a default variable
#     wallet =  f"${balance - cost}"
#     if wallet < 0:
#         return "You can not afford this"
#     else:
#         return wallet
# cost = float(input("How much is the item? "))       
# balance(balance = "70", cost = cost) # By using Keywords you can put arguments in any order

# print("1","2","3","4","5","6", sep="-") # The sep keyword seperates each string with the chosen str


#                   Number 25 (Arbritrary arguments)


# def add(*stock_argument): # Turns into a tuple
#     print(type(stock_argument))
#     total = 0
#     for arg in stock_argument:
#         total += arg
#     return total
# print(add(1,2,3,4)) # 10

# def add(**stock_argument): # Turns into a dictionary
#     print(type(stock_argument)) #dict
#     for key, value in stock_argument.items():
#         print(f"{key}: {value}")
# print(add(num1 = 1,num2 = 2,num3 = 3,num4 = 4))

# def add(*stock_argument1, **stock_argument2): # Can have both a arg and a kwarg
#     print(type(stock_argument1))
#     total = 0
#     for arg in stock_argument1:
#         total += arg
#     print(total)
#     print(type(stock_argument2)) #dict
#     for key, value in stock_argument2.items():
#         print(f"{key}: {value}")

# print(add(num1 = 1,num2 = 2,num3 = 3,num4 = 4))


#                   Number 26 (Iterables)


# numbers = (1, 2, 3, 4, 5)
# for number in reversed(numbers):
#     print*number

# fruits = {"apple", "orange", "banana", "coconut"}
# for fruit in fruits:
#     print(fruit)

# name = "John Doe"
# for charecter in name:
#     print(charecter)

# dictionary = {
#     "A": 1,
#     "B": 2,
#     "C": 3
# }
# for key in dictionary.values():
#     print(key)


#                   Number 27 (Membership operators)


# word = "FOOTBALL"
# letter = "A"

# if letter in word:
#     print("A is in the word")
# elif letter not in word:
#     print("A is not in the word")

# grades = ["A", "B", "C", "D"]
# letter = "B"

# if letter in grades:
#     print("Someone got a B")
# elif letter not in grades:
#     print("No one gor a B")


#                   Number 28 (List comprehension)


# user_inputs = []
# for x in range(1,11):
#     user_inputs.append(input("Enter whatever you want: "))

# double = [x * 2 for x in range(1,11)]
# quad = [y * 2 for y in range(1,11)]

# fruits = ["apple", "banana", "orange"]
# fruits = [fruits.upper() for fruit in fruits]
# print(fruits)

# fruits = [fruits.upper() for fruit in ["apple", "banana", "orange"]]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, 7, -8] 
# positive_number = [num for num in numbers >= 0]
# even_number = [num for num in numbers if num % 2 == 0]

# print(positive_number)
# print(even_number)


#                   Number 29 (Match-Case statements)


# def day_of_week(day):
#     match day:
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Teusday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"
#         case _: # any other statements
#             return "Invalid"

# print(day_of_week(1))
# print(day_of_week(7))
# print(day_of_week("Monkey"))

# def day_of_week(day):
#     match day:
#         case "Saturday" | "Sunday": # | means or
#             return "It is a weekend"
#         case "Monday" | "Teusday" | "Wednesday" | "Thursday" | "Friday":
#             return "It is a weekday"
#         case _:
#             return "Invalid"
 
# print(day_of_week("Saturday"))
# print(day_of_week(input("What day is it today: ")))
# print(day_of_week("Monkey"))


#                   Number 30 (Module)


# print(help("modules")) # shows list of different modules
# print(help("math")) # Import math

# import math as m # now each time you call math you use m
# print(m.pi)

# from math import pi
# print(pi) # this may cause variable name conflicts

# To create a module, create a new python file within the same folder as your original file, create your varibles and functions, then in your original python file, import the new files name, now you can access the everything in the new tab


#                   Number 31 (Scope resolution)


#  - LEGB rule - Local, Enclosed, Global, Built-in

