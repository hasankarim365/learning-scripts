capitals = {
    "USA": "Washington D.C.", 
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
    }

print(dir(capitals))
print(help(capitals))
print(capitals.get("USA"))

capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(f"{key}: {value}")