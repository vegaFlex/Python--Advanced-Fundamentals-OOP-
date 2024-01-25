command = input()
courses = {}

while not command == 'end':
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    command = input()

courses = sorted(courses.items(), key=lambda kvp: (-len(kvp[1]), kvp[1].sort()))

for course, students in courses:
    print(f'{course}: {len(students)}')

    for name in students:
        print(f'-- {name}')



