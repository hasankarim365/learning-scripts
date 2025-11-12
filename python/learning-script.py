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

# def func1():
#     a = 1 # local variable (only works within the function)
#     global b # the global keyword changes the local variable to a global variable
#     b = 32
#     print(a * b)

#     def func2():
#         #a = 2   #as "a" is hashed out, func2 will use the enclosed version of "a" which is 1
#         print(a * x)
#     func2()
    

# x = 3 # global variable as it is not enclosed within a function, so can be called anywhere
# func1()
# print(b) #the global keyword only works after the function has been called

# from math import e

# def func3():
#     print(e) # Built-in variable

# e = 5 #If we look at the LEGB rule, global is before built in so "e = 3" is invoked
# func3()


#                   Number 32 (Dunder Name)


# def main():
#     print("lorem ipsum dolet sit amet")

# if __name__ == "__main__": # means execute this code if this .py script is being run directly, as opposed to being imported to another file
#     main()


#                   Number 33 (Object Oriented Programming)


# Object oriented programming is when you program on object passed on its related attributes (variables) and methods (functions)
# class = (blueprint) used to design the structure and layout of an object

# class Car: # for better organisations you can cut the class onto another file, then import the file, (from "file" import Car)
#     def __init__(self, model, year,colour, for_sale): # this method is needed to create objects and works similar to a function
#         #self means this object we are currently working with (car1, car2, car3)
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.for_sale = for_sale
    
#     def drive(self): #This method is identical to all methods
#         print(f"Drive the {self.colour} {self.model}")

#     def stop(self):
#         print(f"Stop the {self.colour} {self.model}")

#     def describe(self):
#         print(f"{self.year} {self.colour} {self.model}")

# car1 = Car("Supra", 2019, "red", False) # as self is already provided we only need 4 arguments
# car2 = Car("Honda", 2023, "blue", True)
# car3 = Car("Mustang", 2025, "black", False)

# print(car1) # this gives us the memory location of the class
# print(car1.model) # you need to access one of the attributes in order to print it
# print(car1.year)
# print(car1.colour)
# print(car1.for_sale)

# print(car2.model)
# print(car2.year)
# print(car2.colour)
# print(car2.for_sale)

# print(car3.model)
# print(car3.year)
# print(car3.colour)
# print(car3.for_sale)

# car1.drive()
# car2.stop()
# car3.describe()


#                   Number 34 (Class Variables)

# class variables = allow you to share data amongst all objects created from that class

# class Student:

#     class_year = 2026
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name #this is an instance variables
#         self.age = age
#         Student.num_students += 1

# student1 = Student("John", 16)
# student2 = Student("Doe", 17)

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)

# print(student1.class_year) # can access class variables from any object
# print(student2.class_year)
# print(Student.class_year) # but it is good practice to access them from the class to avoid any confusion

# print(Student.num_students)
# student3 = Student("Ed", 16)

# print(Student.num_students)
# print(f"In the {Student.class_year} graduating year, there are {Student.num_students} students")


#                   Number 35 (Inheritence)

# class Father:
#     height = "182"
#     color = "pink"
# class Son(Father): # the son class was given the charecteristics of the father class
#     pass

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} eating")
#     def sleep(self):
#         print(f"{self.name} sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("bark")
        

# class Cat(Animal):
#     def speak(self):
#         print("meow")

# class Mouse(Animal):
#     def speak(self):
#         print("squeek")

# dog = Dog("Scooby")
# cat = Cat("George")
# mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
# dog.speak()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()
# cat.speak()

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()
# mouse.speak()


#                   Number 36 (Multiple Inheritence)

# class Prey():
#     def __init__(self, name):
#         self.name = name
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator():
#     def __init__(self, name):
#         self.name = name
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator): # This is multiple inheritence, which is when a children class inherits from two parent classes
#     pass

# rabbit = Rabbit("Hops")
# hawk = Hawk("Tony")
# fish = Fish("Guppy")

# fish.flee()
# fish.hunt()

# rabbit.flee()
# hawk.hunt()


#                   Number 37 (Multilevel Inheritence)

# class animal():
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")

# class Prey(animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey): # This is multilevel inheritence, which is where when a children class inherits from another children class
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Hops")
# hawk = Hawk("Tony")
# fish = Fish("Guppy")

# fish.eat()
# rabbit.eat()
# hawk.eat()


#                   Number 38 (Super function)
 
# class shapes:
#     def __init__(self, colour, filled):
#         self.colour = colour
#         self.filled = filled

# class Circle(shapes):
#     def __init__(self, colour, filled, radius):
#         super().__init__(colour, filled)
#         self.radius = radius

# class Square(shapes):
#     def __init__(self, colour, filled, width):
#         super().__init__(colour, filled)
#         self.width = width

# class Triangle(shapes):
#     def __init__(self, colour, filled, width, height):
#         super().__init__(colour, filled) # This is the super function, which is a function used in a child class to call methods from a parent class, which is called a superclass.
#         #It allows you to extend the functionalit of the inherited methods
#         self.width = width
#         self.height = height

# circle = Circle("black", "filled", "5")
# square = Square(colour = "red", filled = "Not filled", width = "3")
# triangle = Triangle(colour = "blue", filled = "Not filled", width = "5", height= "6")

# print(circle.colour)
# print(circle.filled)
# print(circle.radius)

# print(square.colour)
# print(square.filled)
# print(square.width)

# print(triangle.colour)
# print(triangle.filled)
# print(triangle.width)
# print(triangle.height)


#                   Number 39 (Polymorphism - inheritence)

# from abc import ABC, abstractmethod

# class Shape():
#     @abstractmethod
#     def __init__(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
 
#     def area(self):
#         return self.base * self.height / 2


# shapes = [Circle(4), Square(5), Triangle(6, 7)]

# for shape in shapes:
#     print(f"{shapes.area()}cm squared")


#                   Number 40 (Static and Instance methods)

# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self): # This is an instance method
#         return f"{self.name} = {self.position}"

#     @staticmethod
#     def is_valid_position(position): # This is a static method
#         valid_position = ["manager", "chef", "waiter", "janitor", "cashier"] 
#         return position in valid_position

# employee1 = Employee("Eugene", "manager")
# employee2 = Employee("Squidward", "cashier") # In an instance method, an instance of the class needs to be accessed to run the method
# employee3 = Employee("Eugene", "chef") 

# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

# Employee.is_valid_position("chef")
# Employee.is_valid_position("Trainer") # In a static method, no instances of the class need to be accesed to run the method


#                   Number 41 (Class methods)

# class Student:

#     count = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student += 1
    
#     def get_info(self):
#         return f"{self.name} : {self.gpa}"
    
#     @classmethod # This is a class method, which is a method that allows operation related the class itself. 
#     def get_count(cls): # It takes cls as an argument, which represents the class itseld
#         return f"Total # of student : {cls.count}"
    
# student1 = Student("Spongebob", 3.2)
# student1 = Student("Patrick", 2.0)
# student1 = Student("Sandy", 4.0)

# print(Student.get_count())


#                   Number 42 (Magic methods)


# class Student:

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa

#     def __str__(self):
#         return f"name: {self.name} gpa: {self.gpa}"

#     def __eq__(self, other):
#         return self.name == other.name

#     def __gt__(self, other):
#         return self.gpa > other.gpa

# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)

# print(student1)
# print(student1 == student2)
# print(student1 > student2)


#                   Number 43 (Property decorator)


# class Rectangle():
#     def __init__(self, width, height):
#             self._width = width # _width tells you and other developers that this avriable is meant to be protected, and thta it must only be used internally
#             self._height = height

#     @property
#     def width(self):
#           return f"{self._width:.1f}cm"
            
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")

# rectangle = Rectangle(3, 4)

# print(rectangle.height)
# print(rectangle.width)

# print(rectangle._height) # gives the raw variable without the cm and not to 1f
# print(rectangle._width)

# rectangle.width = 0
# rectangle.width = -1

# del rectangle.width
# del rectangle.height


#                   Number 44 (Decorators)


# def add_sprinkles(func):
#     def wrapper(): # without this wrapper function as soon as you run the program, @add sprinkls would run
#         print("*You add sprinkles*")
#         func()
#     return wrapper


# @add_sprinkles # Decorators modify the function, without modifying the base code
# def get_ice_cream():
#     print("Here is your ice cream")


#                   Number 45 (Exception handling)

# try: #any code that could cause an error would be placed within the try block
#     number = int(input("Enter a number: "))
#     print(1/number)
# except  ZeroDivisionError:
#     print("You cant divide by 0")
# except ValueError:
#     print("You cant divide a number by a string")
# finally:
#     print("DO something")


#                   Number 46 (File Detection)


# import os # This module allows python to interact with the Operating System

# filepath = "text.txt"

# if os.path.exists(filepath): # checks if the file exists
#     print("File found")
#     if os.path.isfile(filepath): # checks if it is a file
#         print("It is a file")
#     elif os.path.isdir(filepath): # checks if it is a directory
#         print("It is a directory")
# else:
#     print("File not found") 


#                   Number 47 (Writing Files)

# file_path = "text.txt"
# with open(file_path, "w") as file: # (with) closes the file after the code is run, ("w") creates a file
#     file.write("Lorem Ipsum")
#     print("created")

# with open(file_path, "x") as file: # ("x") creates a file if thefile does not exist
#     file.write("Lorem Ipsum")
#     print("created")

# with open(file_path, "a") as file: # ("a") appends the data that is within the file
#     file.write("Lorem Ipsum")
#     print("created")

# import json
# file_path = "text.json"

# with open(file_path, "w") as file:
#     json.dump("Lorem Ipsum")
#     print("json created")

# import csv
# file_path = "text.csv"

# with open(file_path, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow("Lorem Ipsum")
#     print("csv created")


#                   Number 48 (Reading Files)


# file_path = "text.txt"

# with open(file_path, "r") as file:
#     content = file.read()
#     print(content)

# import json
# file_path = "text.json"

# with open(file_path, "r") as file:
#     content = json.load(file)
#     print(content)

# import csv
# file_path = "text.csv"

# with open(file_path, "r") as file:
#     content = csv.reader(file)
#     print(content)


#                   Number 49 (Import datetime)


# import datetime

# date = datetime.date(2025, 1 , 27)
# now = datetime.date.today()
# print(f"This is a date: {date}. \n  This is the date now: {now}")

# time = datetime.time(9, 5, 0)
# time_now = datetime.datetime.now()

# print(time)
# print(time_now)

# now = now.strftime("%d/%m/%Y, %H:%M:%S")


#                   Number 49 (Multithreading)


    