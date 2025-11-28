try: #any code that could cause an error would be placed within the try block
    number = int(input("Enter a number: "))
    print(1/number)
except  ZeroDivisionError:
    print("You cant divide by 0")
except ValueError:
    print("You cant divide a number by a string")
finally:
    print("DO something")
