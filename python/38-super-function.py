class shapes:
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled

class Circle(shapes):
    def __init__(self, colour, filled, radius):
        super().__init__(colour, filled)
        self.radius = radius

class Square(shapes):
    def __init__(self, colour, filled, width):
        super().__init__(colour, filled)
        self.width = width

class Triangle(shapes):
    def __init__(self, colour, filled, width, height):
        super().__init__(colour, filled) # This is the super function, which is a function used in a child class to call methods from a parent class, which is called a superclass.
        #It allows you to extend the functionalit of the inherited methods
        self.width = width
        self.height = height

circle = Circle("black", "filled", "5")
square = Square(colour = "red", filled = "Not filled", width = "3")
triangle = Triangle(colour = "blue", filled = "Not filled", width = "5", height= "6")

print(circle.colour)
print(circle.filled)
print(circle.radius)

print(square.colour)
print(square.filled)
print(square.width)

print(triangle.colour)
print(triangle.filled)
print(triangle.width)
print(triangle.height)