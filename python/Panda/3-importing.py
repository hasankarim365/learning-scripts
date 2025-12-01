import pandas as pd

# CSV Files

df = pd.read_csv("external_data/pokemon.csv") # The read_csv() is a function, so is not capitalised
print(df) 
# print(df.to_string()) # This prints all the rows

# JSON

df  = pd.read_json("external_data/pokedex.json") # The read_json() is a function, so is not capitalised
print(df) # This makes a DataFrame out of the JSON file, and gives you the amount of columns and rows in the DataFrame, but it only shows the first and last five rows
# print(df.to_string()) # This prints all the rows

