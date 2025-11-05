# Object oriented programming is when you program on object passed on its related attributes (variables) and methods (functions)
# class = (blueprint) used to design the structure and layout of an object

class Car: # for better organisations you can cut the class onto another file, then import the file, (from "file" import Car)
    def __init__(self, model, year,colour, for_sale): # this method is needed to create objects and works similar to a function
        #self means this object we are currently working with (car1, car2, car3)
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
    
    def drive(self): #This method is identical to all methods
        print(f"Drive the {self.colour} {self.model}")

    def stop(self):
        print(f"Stop the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")

car1 = Car("Supra", 2019, "red", False) # as self is already provided we only need 4 arguments
car2 = Car("Honda", 2023, "blue", True)
car3 = Car("Mustang", 2025, "black", False)

print(car1) # this gives us the memory location of the class
print(car1.model) # you need to access one of the attributes in order to print it
print(car1.year)
print(car1.colour)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.colour)
print(car3.for_sale)

car1.drive()
car2.stop()
car3.describe()