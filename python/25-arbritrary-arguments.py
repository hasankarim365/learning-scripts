def add(*stock_argument): # Turns into a tuple
    print(type(stock_argument))
    total = 0
    for arg in stock_argument:
        total += arg
    return total
print(add(1,2,3,4)) # 10

def add(**stock_argument): # Turns into a dictionary
    print(type(stock_argument)) #dict
    for key, value in stock_argument.items():
        print(f"{key}: {value}")
print(add(num1 = 1,num2 = 2,num3 = 3,num4 = 4))

def add(*stock_argument1, **stock_argument2): # Can have both a arg and a kwarg
    print(type(stock_argument1))
    total = 0
    for arg in stock_argument1:
        total += arg
    print(total)
    print(type(stock_argument2)) #dict
    for key, value in stock_argument2.items():
        print(f"{key}: {value}")

print(add(num1 = 1,num2 = 2,num3 = 3,num4 = 4))