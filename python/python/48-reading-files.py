file_path = "text.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

import json
file_path = "text.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)

import csv
file_path = "text.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    print(content)
