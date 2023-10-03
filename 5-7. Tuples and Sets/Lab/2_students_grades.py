n = int(input())

students = {}

for _ in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")
