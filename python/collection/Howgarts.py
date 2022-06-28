from asyncore import read
import csv
from itertools import count
from cs50 import get_string

houses = {
    "G" : 0,
    "H" : 0,
    "R" : 0,
    "S" : 0
}

with open("hogwarts.csv", "a") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        house = row[1]
        houses[house] += 1

for house in houses:
    counter = houses[house]
    print(f"{house} : {counter}")