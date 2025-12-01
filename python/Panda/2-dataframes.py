import pandas as pd

# A dataframe is a tabular structure wiith rows and columns, making them two dimensional

days = {"Monday": [1, 8, 15],
        "Tuesday": [2, 8, 16],
        "Wednesday": [3, 10, 17],
        "Thursday": [4, 11, 18],
        "Friday": [5, 12, 19],
        "Saturday": [6, 13, 20]}
df = pd.DataFrame(days) # This a DataFrame CONSTRUCTOR not a function, so it is capitalised
print(df) # This prints the dictionary as a DataFrame, where the key would the name of the column, and the value as the elements of the dataFrame

df = pd.DataFrame(days, index = ["Week1", "Week2", "Week3"]) # This changes the index of the dictionary to anything you choose
print(df)

print(df.loc["Week1"]) # This prints all the elements at index week1
print(df.iloc[0]) # This prints all the elements in the row(0)

df["Sunday"] =  [7, 14, 21] # This creates a new column called Sunday in the DataFrame
print(df)

new_row = pd.DataFrame([{"Monday": 22, "Tuesday": 23, "Wednesday": 24, "Thursday": 25, "Friday": 26, "Saturday": 27, "Sunday": 28}], index = ["Week4"])
df = pd.concat([df, new_row]) # This adds the new row to the DataFrame
print(df)

new_rows = pd.DataFrame([{"Monday": 29, "Tuesday": 30, "Wednesday": 31, "Thursday": 32, "Friday": 33, "Saturday": 34, "Sunday": 35},
                        {"Monday": 36, "Tuesday": 37, "Wednesday": 38, "Thursday": 39, "Friday": 40, "Saturday": 41, "Sunday": 42}], index = ["Week4", "Week5"])
df = pd.concat([df, new_rows]) # This add the new rows to the DataFrame
print(df)
