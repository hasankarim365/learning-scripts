file_path = "text.txt"
with open(file_path, "w") as file: # (with) closes the file after the code is run, ("w") creates a file
    file.write("Lorem Ipsum")
    print("created")

with open(file_path, "x") as file: # ("x") creates a file if thefile does not exist
    file.write("Lorem Ipsum")
    print("created")

with open(file_path, "a") as file: # ("a") appends the data that is within the file
    file.write("Lorem Ipsum")
    print("created")

import json
file_path = "text.json"

with open(file_path, "w") as file:
    json.dump("Lorem Ipsum")
    print("json created")

import csv
file_path = "text.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow("Lorem Ipsum")
    print("csv created")
