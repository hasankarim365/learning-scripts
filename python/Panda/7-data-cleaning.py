import pandas as pd

# Data cleaning is the process of fixing/removing incomplete, incorrect, or irrelevant data.

df = pd.read_csv("external_data/pokemon.csv")

# Drop irrelevant columns
df = df.drop(columns=["Legendary", "Generation"]) # This drops the columns "Legendary" and "Generation"

# Handle missing data
df = pd.read_csv("external_data/pokemon.csv")
df = df.dropna(subset=["Type 2"]) # This drops any rows in the column Type2 that do not have any values

df = pd.read_csv("external_data/pokemon.csv")
df = df.fillna({"Type 2": "None"}) # This replaces any rows in the column Type2 that do not have any values, with "None"

# Fix inconsistant values
df = pd.read_csv("external_data/pokemon.csv")
df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS",
                                    "Fire": "FIRE"}) # This replaces any instances of Fire and Grass in Type1 to FIRE and GRASS

# Standardise Text
df = pd.read_csv("external_data/pokemon.csv")
df["Name"] = df["Name"].str.lower() # This makes all the elements in Name, lowercase

# Fix data types
df["Legendary"] = df["Legendary"].astype(bool)

# Remove duplicate values
df = pd.read_csv("external_data/pokemon_dup.csv")
df = df.drop_duplicates() # This drops any duplicates in the dataFrame

print(df)