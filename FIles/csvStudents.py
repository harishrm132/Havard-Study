import csv

students = []

with open("students.csv") as file:
    # reader = csv.reader(file)
    # for name, age in reader:
    #     students.append({"name": name, "age": age})
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "age": row["age"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} age is {student['age']}")