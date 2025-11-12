class animal():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): # This is multilevel inheritence, which is where when a children class inherits from another children class
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Hops")
hawk = Hawk("Tony")
fish = Fish("Guppy")

fish.eat()
rabbit.eat()
hawk.eat()