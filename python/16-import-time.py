import time

my_time = int(input("Enter time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1) # Between each iteration delay for 1 second