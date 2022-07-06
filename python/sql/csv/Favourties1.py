import csv
import re

counter = 0
title = input("Title: ").strip().upper()

with open("Favourties.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        t = row["title"].strip().upper()
        if re.search(f"^({title})$", t, flags=re.IGNORECASE):
            counter += 1

        

print(f"Total : {counter}")