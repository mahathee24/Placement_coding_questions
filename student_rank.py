class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def __str__(self):
        return f"{self.name}: {self.marks}"

students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))
    students.append(Student(name, marks))
    print("Student added successfully")

def view_topper():
    if not students:
        print("No students found")
        return
    topper = max(students, key=lambda s: s.marks)
    print(f" Topper: {topper.name} with {topper.marks} marks")

def view_individual_status():
    name = input("Enter student name to search: ")
    for student in students:
        if student.name.lower() == name.lower():
            print(f"{student.name} scored {student.marks} marks")
            return
    print("Student not found")

def view_ranks():
    if not students:
        print("No students found")
        return
    ranked_students = sorted(students, key=lambda s: s.marks, reverse=True)
    print(" Student Rankings:")
    for i, student in enumerate(ranked_students, start=1):
        print(f"{i}. {student.name} - {student.marks} marks")
    print()

def view_status_menu():
    while True:
        print("--- View Status Menu ---")
        print("a. View Topper")
        print("b. View Individual Student Status")

        print("c. View Rank of Students")
        print("d. Back to Main Menu")
        choice = input("Enter your choice (a/b/c/d): ")

        if choice == 'a':
            view_topper()
        elif choice == 'b':
            view_individual_status()
        elif choice == 'c':
            view_ranks()
        elif choice == 'd':
            break
        else:
            print("Invalid choice. Try again")

def main_menu():
    while True:
        print("-- Main Menu ---")
        print("1. Add Student")
        print("2. View Status")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_status_menu()
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Invalid choice")

main_menu()
