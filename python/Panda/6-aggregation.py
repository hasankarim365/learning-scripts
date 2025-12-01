import pandas as pd

# aggregate fuctions are functions that reduce a set of values into a single summary value

df = pd.read_csv("external_data/pokemon.csv")

# Whole DataFrame

print(df.mean(numeric_only=True)) # This finds the mean of any columns that are numerical
print(df.sum(numeric_only=True)) # This finds the sum of any columns that are numerical
print(df.min(numeric_only=True)) # This finds the minimum number of any columns that are numerical
print(df.max(numeric_only=True)) # This finds the mean of any columns that are numerical
print(df.count(numeric_only=True)) # This finds the number of elements within a column

# Single Column

print(df["HP"].mean())    
print(df["HP"].sum()) 
print(df["HP"].min()) 
print(df["HP"].max()) 
print(df["HP"].count())

# Grouping

group = df.groupby("Type 1") # This groups each individual type
print(group["HP"].mean())

