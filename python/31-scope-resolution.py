#  - LEGB rule - Local, Enclosed, Global, Built-in

def func1():
    a = 1 # local variable (only works within the function)
    global b # the global keyword changes the local variable to a global variable
    b = 32
    print(a * b)

    def func2():
        #a = 2   #as "a" is hashed out, func2 will use the enclosed version of "a" which is 1
        print(a * x)
    func2()
    

x = 3 # global variable as it is not enclosed within a function, so can be called anywhere
func1()
print(b) #the global keyword only works after the function has been called

from math import e

def func3():
    print(e) # Built-in variable

e = 5 #If we look at the LEGB rule, global is before built in so "e = 3" is invoked
func3()
