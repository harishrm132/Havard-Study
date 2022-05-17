students = []

with open("students.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        student = {"name": name, "age": age}
        # student["name"] = name
        # student["age"] = age
        students.append(student)

# def get_name(student):
#     return student["name"]
# for student in sorted(students, key=get_name):

# Lambda - Anonymous function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} age is {student['age']}")