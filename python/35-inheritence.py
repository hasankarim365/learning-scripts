class Father:
    height = "182"
    color = "pink"
class Son(Father): # the son class was given the charecteristics of the father class
    pass

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} eating")
    def sleep(self):
        print(f"{self.name} sleeping")

class Dog(Animal):
    def speak(self):
        print("bark")
        

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeek")

dog = Dog("Scooby")
cat = Cat("George")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()
