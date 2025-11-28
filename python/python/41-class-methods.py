class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student += 1
    
    def get_info(self):
        return f"{self.name} : {self.gpa}"
    
    @classmethod # This is a class method, which is a method that allows operation related the class itself. 
    def get_count(cls): # It takes cls as an argument, which represents the class itseld
        return f"Total # of student : {cls.count}"
    
student1 = Student("Spongebob", 3.2)
student1 = Student("Patrick", 2.0)
student1 = Student("Sandy", 4.0)

print(Student.get_count())