import pandas as pd

df = pd.read_csv("external_data/pokemon.csv")

# Selection by columns

print(df["Name"]) # This selects the column Name and creates a series, it prints the amount of rows and the metadata on the datatype, but it only shows the first and last 5 rows
# print(df["Name"].to_string()) # This print all the rows

print(df[["Name", "Total", "HP"]]) # This selects the columns Name, Total, and HP and makes a DataFrame, it prints the amount of rows, but it only shows the first and last 5 rows
print(df[["Name", "Total", "HP"]]) # This prints all rows

# Selection by ROW/S

print(df.loc[0]) # This would select the row 0 and creates a series

df = pd.read_csv("external_data/pokemon.csv", index_col= "Name") # This changes the index of the DataFrame to the colum you selected
print(df.loc["Charmander"])

print(df.loc["Charmander", ["#", "HP", "Attack",]]) # This specifies which columns you want to see at the index
print(df.loc["Charmander":"Charizard"]) # This is a splice operator, it states where to start and end selecting

print(df.iloc[0:11]) # This selects the rows zero through ten, as the end operation is exclusive
print(df.iloc[0:11:2]) # This selects the first row then every second row
print(df.iloc[0:11, 0:3]) # This selects the rows zero through ten, and the columns zero through two