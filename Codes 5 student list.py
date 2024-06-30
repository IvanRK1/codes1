def menu():
    print("Stundent manager system")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Find a student")
    print("4. Print the list of students")
    print("5. Exit")


def add_student(students):
    name = input("Enter the name of the student to add")
    students.append(name)
    print(f"{name} has been added to the list")


def remove_student(students):
    name = input("Enter the name of the student to remove")
    if name in students:
        students.remove(name)
        print(f"{name} has been removed from the list")
    else:
        print(f"{name} is not in the list")

def find_student(students):
    name = input("Enter the name of the student to find")
    if name in students:
        index = students.index(name)
        print(f"{name} is at index {index}")
    else:
        print(f"{name} is not in the list")

def print_students(students):
    print("List of students", students)

def main():
    students = ['Alice', 'Bob', 'David', 'Eva']
    while True:
        menu()
        choice = input("Enter your choice ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            print_students(students)
        elif choice == "5":
            print("Exiting the Student Management System")
            break
        else:
            print("Invalid choice, please try again")
if __name__ == "__main__":
    main()
