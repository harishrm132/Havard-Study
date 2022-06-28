#Column A - ColA
#Column B - ColB

colA = ""
colB = ""

def IsMatch(str1, str2):
    for val1 in str1.split(" "):
        for val2 in str2.split(" "):
            if val1 in val2 or val2 in val1:
                return True
    return False


IsMatch(colA, colB)