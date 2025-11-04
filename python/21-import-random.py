import random

print(help(random)) # shows all methods

number = random.randint(1, 10) # random int
print(number)

number = random.random() # Random float
print(number)

workers = ("Sam", "Mark", "Paul")
cleaning_duty = random.choice(workers)
print(cleaning_duty)

ordered_list = [1,2,3,4,5,6,7,8,9]
unordered_list = random.shuffle(ordered_list)
print(unordered_list)
