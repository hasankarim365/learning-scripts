def add_sprinkles(func):
    def wrapper(): # without this wrapper function as soon as you run the program, @add sprinkls would run
        print("*You add sprinkles*")
        func()
    return wrapper


@add_sprinkles # Decorators modify the function, without modifying the base code
def get_ice_cream():
    print("Here is your ice cream")
