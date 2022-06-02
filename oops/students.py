
class Student:
    def __init__(self, name, house, patrnous):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
        self.patrnous = patrnous

    def __str__(self):
        return f"{self.name} from {self.house} has {self.patrnous}"
    
    def charm(self):
        if self.patrnous == "Stag":
            return "🐎"
        elif self.patrnous == "Otter":
            return "🦦"
        elif self.patrnous == "Terrier":
            return "🐶"
        else:
            return "💣"

    def __repr__(self) -> str:
        pass


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print("Exceptco petronum!!!")
    print(student.charm())

def get_student():
    name = input("Name:")
    house = input("House:")
    patrnous = input("Patrnous:")
    try:
        return Student(name, house, patrnous)
    except ValueError:
        ...


if __name__ == "__main__":
    main()