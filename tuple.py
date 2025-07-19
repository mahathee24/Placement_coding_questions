students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]

# Calculate percentage and store it
for student in students:
    total = sum(student["marks"])
    percentage = (total / 300) * 100
    student["percentage"] = round(percentage, 2)  # round to 2 decimal places

# Sort students by percentage in descending order
students_sorted = sorted(students, key=lambda x: x["percentage"], reverse=True)

# Display
for student in students_sorted:
    print(f"Name: {student['name']}, Department: {student['dept']}, Percentage: {student['percentage']}%")
