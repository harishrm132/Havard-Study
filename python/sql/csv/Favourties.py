import csv

titles = {}

with open("Favourties.csv", "r") as file:
    # reader = csv.reader(file)
    # #Ignore the first row of the file
    # next(reader)
    # print(row[1]) 
    reader = csv.DictReader(file)
    for row in reader:
        t = row["title"].strip().upper()
        if not t in titles:
            titles[t] = 0
        titles[t] += 1
        # titles = []
        # if not t in titles:
        #     titles.append(t)
        # titles = set()
        # titles.add(t)

# def get_value(title):
#     return titles[title]

for t in sorted(titles, key=lambda t: titles[t], reverse=True):
    print(t, titles[t])

print(len(titles))