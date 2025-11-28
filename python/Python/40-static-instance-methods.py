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
