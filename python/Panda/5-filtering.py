import pandas as pd

# Filtering is keeping the rows that match the conditions given

df = pd.read_csv("external_data/pokemon.csv")
fast_pokemon = df[df["Speed"] > 95] # This keeps the pokemon that have a speed greater than 95
print(fast_pokemon)

legendary_pokemon = df[df["Legendary"] == True] # This keeps the pokemon that are Legendary
print(legendary_pokemon)

legendary_pokemon = df[df["Legendary"]] # This is the same as the filtering above, if the element is a Boolean you do not need to specify
print(legendary_pokemon)

water_pokemon = df[df["Type 1" == "Water"] | ["Type 2" == "Water"]] # This keeps pokemon that have a Type1 of water OR a Type2 of water
print(water_pokemon)

pureFire_pokemon = df[df["Type 1" == "Fire"] & ["Type 2" == "Fire"]] # This keeps pokemon that have a Type1 of Fire AND a Type2 of Fire
print(pureFire_pokemon)
