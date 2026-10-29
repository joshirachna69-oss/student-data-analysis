students = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 76,
    "Neha": 88,
    "Priya": 95
}

average = sum(students.values()) / len(students)
topper = max(students, key=students.get)

print("Student Marks Analysis")
print("Average marks:", average)
print("Topper:", topper)
print("Highest marks:", students[topper])
