from asyncore import write
import csv

name = input("name: ")
age = int(input("age: "))

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writerow({"name": name, "age": age})