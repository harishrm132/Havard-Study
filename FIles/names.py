

# region Input reading 2    
# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello,{name}")
# endregion 

# region Input reading 1 

# with open("names.txt", "r") as file:
#     lines = file.readlines()
# print(lines)

# for line in lines:
#     print("Hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

# endregion

# region Input Writing - 2
# name = input("Whats your name?")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# endregion

# region p-1
# names = []

# for _ in range(3):
#     names.append(input("Name: "))

# for name in sorted(names):
#     print(f"{name}")
# endregion