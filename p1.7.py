students = {
    "A": 80,
    "B": 90,
    "C": 70,
    "D": 85,
    "E": 95
}

for name in students:
    print(name, ":", students[name])

total = sum(students.values())
average = total / 5

print("Class Average =", average)

highest = max(students, key=students.get)
print("Highest Marks Student =", highest)
print("Marks =", students[highest])
