user_inputs = []
for x in range(1,11):
    user_inputs.append(input("Enter whatever you want: "))

double = [x * 2 for x in range(1,11)]
quad = [y * 2 for y in range(1,11)]

fruits = ["apple", "banana", "orange"]
fruits = [fruits.upper() for fruit in fruits]
print(fruits)

fruits = [fruits.upper() for fruit in ["apple", "banana", "orange"]]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 7, -8] 
positive_number = [num for num in numbers >= 0]
even_number = [num for num in numbers if num % 2 == 0]

print(positive_number)
print(even_number)