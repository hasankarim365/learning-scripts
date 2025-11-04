fruits = ["apple", "orange", "banana"]
vegetables = ["celery", "carrots", "potatoes"]

groceries = [fruits, vegetables]
print(groceries)
print(groceries[0][1]) # orange

groceries = ["apple", "orange", "banana"], ["celery", "carrots", "potatoes"]
print(groceries)
print(groceries[0][1]) # orange


for x in groceries:
    for food in x:
        print(food) # prints each member of the list individually

