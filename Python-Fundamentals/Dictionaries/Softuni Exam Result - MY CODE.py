users = {}
all_users = {}
command = input()
banned_users = {}

while not command == 'exam finished':
    if 'banned' not in command:

        user_info = command.split('-')
        name = user_info[0]
        course = user_info[1]
        points = int(user_info[2])

        if name not in users:
            users[name] = {}
            all_users[name] = {}

        if course not in users[name]:
            users[name][course] = []
            all_users[name][course] = []

        users[name][course].append(points)
        all_users[name][course].append(points)

    elif 'banned' in command:
        ban_info = command.split('-')
        ban_user = ban_info[0]

        for key, value in users.items():
            if ban_user in key:
                banned_users[key] = value
                all_users[key] = value
                users.pop(key)
                break

        command = input()

        if command == 'exam finished':
            break

    command = input()
for name, value in users.items():
    for curr_course, grade in value.items():
        users[name][curr_course] = max(grade)

new_dict = {}

for name, value in users.items():
    for grade in value.values():
        new_dict[name] = grade

sorted_dict = sorted(new_dict.items(), key=lambda x: (-x[1], x[0]))
print('Results:')

for key_name, value_grade in sorted_dict:
    print(f'{key_name} | {value_grade}')

print(f"Submissions:")

all_grades = {}

for name2, value2 in all_users.items():
    for course2, grade2 in value2.items():
        if course2 not in all_grades:
            all_grades[course2] = 0
        all_grades[course2] += len(grade2)

for k, v in sorted(all_grades.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k} - {v}")



