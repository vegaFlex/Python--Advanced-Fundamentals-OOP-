n = int(input())
students = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {}
for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        filtered_students[name] = avg_grade


sorted_students = sorted(filtered_students.items(), key=lambda x: -x[1])

for name, grade in sorted_students:
    print(f"{name} -> {grade:.2f}")



