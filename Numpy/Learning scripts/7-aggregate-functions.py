import numpy as np

#aggregate functions summarize data and typically return a single value

array = np.array([[1,2,3,4,5], 
                  [6,7,8,9,10]])

print(np.sum(array)) # This aggragate function finds the sum of an array
print(np.mean(array)) # This aggragate function finds the mean of an array
print(np.std(array)) # This aggragate function finds the standard deviation of an array
print(np.var(array)) # This aggragate function finds the variance of an array
print(np.min(array)) # This aggragate function finds the smallest value in an array
print(np.max(array)) # This aggragate function finds the largest value in an array
print(np.argmin(array)) # This aggragate function finds the position of the smallest value in an array
print(np.argmax(array)) # This aggragate function finds the position of the largest value in an array

print(np.sum(array, axis=0)) # This aggragate function finds the sum of each column in an array
print(np.sum(array, axis=1)) # This aggragate function finds the sum of each row in an array