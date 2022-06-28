from students import Student

def main():
    student = Student.get()  
    print(f"{student.name} from {student.house}")

if __name__ == "__main__":
    main()