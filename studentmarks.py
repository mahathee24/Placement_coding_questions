 #need to get  names from the user and  subject marks for one student and display the names with percentage in format of 1.Raju:99% ,2.Pani:70% ,Ravi:54%,Ana:77% and jack :87%

#to get names and marks of students and display their percentagestudents
students = []

for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    total = 0
    for j in range(3):
        mark = int(input(f"Enter the mark for subject {j+1}: "))
        total += mark
    percentage = total // 3
    students.append({"name": name, "percentage": percentage})

print("\nStudent Percentages:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student['name']} : {student['percentage']}%")
