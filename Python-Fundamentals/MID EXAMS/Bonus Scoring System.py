students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
total_student_attendances = 0

for student in range(1, students + 1):
    student_attendances = int(input())

    total_bonus = student_attendances / lectures * (5 + additional_bonus)

    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        total_student_attendances = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {total_student_attendances} lectures.")

