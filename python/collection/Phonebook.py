# people = {
#     "Hari" : "7708889121",
#     "Aadhi" : "9600531782"
# }

# name = input("Get Name:").title()
# if name in people:
#     print(f"Number: {people[name]}")

import csv
from cs50 import get_string

name = get_string("Name: ")
no = get_string("Number: ")

# file = open("Phonebook.csv", "a")
# file.close()
with open("Phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, no])

