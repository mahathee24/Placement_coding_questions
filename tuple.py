students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]

# Calculate average and store it
for student in students:
    total = sum(student["marks"])
    avg = total // len(student["marks"])  # integer average
    student["average"] = avg

# Sort by average marks in descending order
students_sorted = sorted(students, key=lambda x: x["average"], reverse=True)

# Display
for student in students_sorted:
    print(f"Name: {student['name']}, Department: {student['dept']}, Average Marks: {student['average']}")
