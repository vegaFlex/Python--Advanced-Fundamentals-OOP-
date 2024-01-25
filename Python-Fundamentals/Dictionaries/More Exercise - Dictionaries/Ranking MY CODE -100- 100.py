contests = {}
line_one = input()
while line_one != 'end of contests':
    valid_contest, valid_pass = line_one.split(':')
    contests[valid_contest] = valid_pass
    line_one = input()

users = {}
line_two = input()
while not line_two == "end of submissions":
    curr_contest, curr_pass, username, points = line_two.split('=>')
    points = int(points)
    if curr_contest in contests and contests[curr_contest] == curr_pass:
        if username not in users:
            users[username] = {curr_contest: points}
        else:
            if curr_contest in users[username]:
                if users[username][curr_contest] < points:
                    users[username][curr_contest] = points
            else:
                users[username][curr_contest] = points
    line_two = input()

best_user = ''
max_points = 0
for user, values in users.items():
    curr_points = 0
    for contest, point in values.items():
        curr_points += point
    if curr_points > max_points:
        max_points = curr_points
        best_user = user

print(f'Best candidate is {best_user} with total {max_points} points.')
print('Ranking:')

for student, courses in sorted(users.items(), key=lambda x: x[0]):
    print(f'{student}')
    for course, points in sorted(courses.items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")















