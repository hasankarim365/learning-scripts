# class variables = allow you to share data amongst all objects created from that class

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name #this is an instance variables
        self.age = age
        Student.num_students += 1

student1 = Student("John", 16)
student2 = Student("Doe", 17)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

print(student1.class_year) # can access class variables from any object
print(student2.class_year)
print(Student.class_year) # but it is good practice to access them from the class to avoid any confusion

print(Student.num_students)
student3 = Student("Ed", 16)

print(Student.num_students)
print(f"In the {Student.class_year} graduating year, there are {Student.num_students} students")
