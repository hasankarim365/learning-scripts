age = input("What is your age: ")

while not age.isdigit(): # loops if age does not consist of only numbers
    print("Enter only number")
    age = input("What is your age: ")
