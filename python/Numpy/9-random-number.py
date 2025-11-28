import numpy as np

rng = np.random.default_rng()
print(rng.integers(1, 7)) # This prints a random number between 1 and 6, as the last number is exclusive
print(rng.integers(low = 1,high =  7)) # The keywords are not nessasary, but they help with readability

print(rng.integers(low = 1,high =  7, size = 3)) # The size keyword is the amount of random generated numbers. The output is stored in a 1-D array
print(rng.integers(low = 1,high =  7, size = (3,2))) # This creates a 2-D array of shape 3, 2

rng = np.random.default_rng(seed = 1) # The seed makes it so rng retains the result
# This is useful if you need to reproduce the same results

# FLoating point numbers

print(np.random.uniform()) # This prints a random floating point number before 1 and 0

np.random.seed(seed = 1)
print(np.random.uniform(-1, 1, (3,2)))

# Shuffle an array

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# Choice at random

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
choice = rng.choice(array)
print(choice)
choice = rng.choice(array, size=2)
print(choice)