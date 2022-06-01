import re

email = input("Email: ").strip()

# ..* to have any charc, any charac (o or more) is same as .+
if re.search("^\w+@(\w\.)?\w+\.(edu|com|gov|in)$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("InValid")