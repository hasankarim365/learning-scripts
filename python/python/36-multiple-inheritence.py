class Prey():
    def __init__(self, name):
        self.name = name
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator():
    def __init__(self, name):
        self.name = name
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # This is multiple inheritence, which is when a children class inherits from two parent classes
    pass

rabbit = Rabbit("Hops")
hawk = Hawk("Tony")
fish = Fish("Guppy")

fish.flee()
fish.hunt()

rabbit.flee()
hawk.hunt()