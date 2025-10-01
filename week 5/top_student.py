# Step 1: Initialize a dictionary of students and their grades
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

# Step 2: Output the list of students and their grades
print("Class Grades:")
for student, grade in grades.items():
    print(f"{student} : {grade}")

# Step 3: Find the highest grade
highest_grade = max(grades.values())

# Step 4: Find the top student(s)
for student, grade in grades.items():
    if grade == highest_grade:
        top_student = student
        break

# Step 5: Print the top student and their grade
print(f"\nTop student: {top_student} with grade {highest_grade}")
