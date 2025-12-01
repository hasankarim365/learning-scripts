import pandas as pd

# Series are 1-dimentional labelled arrays that can hold any data type

# Lists

data = [1, 2, 3, 4, 5]
series = pd.Series(data) # This a Series CONSTRUCTOR not a function, so it is capitalised
print(series) # This prints the list as a series along with metadata on the datatpye of the list, which would be int64

data = [1.1, 2.2, 3.3, 4.4, 5.5]
series = pd.Series(data)
print(series) # As the data is a list the datatype is now float64

data = [1, 2, 3, 4, 5]
series = pd.Series(data, index = ["a", "b", "c", "d", "e"])# This changes the index of the series to what you choose
print(series)

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data, index = ["a", "b"]) # If the index does not match the size of the library, then it will show a ValueError
# print(series)

data = [1, 2, 3, 4, 5]
series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
print(series.loc["a"]) # This will give you the element at the index "a"
# print(series.loc["x"]) # If the index does not exist, then it will show a ValueError

series.loc["c"] = 999 # This allows you to change elements in a series
print(series)

data = [1, 2, 3, 4, 5]
series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
print(series.iloc[0]) # This will give the element at intiger position 0

print(series[series > 3]) # This prints the elements that are greater than 3, with their indexes

# Dictionary

week = {"Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7,}
series = pd.series(week)
print(series) # Using a dictionary means that the key is used as the index,, while the value the value is the element

# All the other processes are the same as with a library