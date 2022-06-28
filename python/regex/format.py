import re

name = input("Name:").strip()

# Walrus Operator - If and Only if
if matches := re.search("^(.+), *(.+)$", name):
    last = matches.groups(1)
    first = matches.groups(2)
    name = f"{first} {last}"

print(f"Hello, {name}")