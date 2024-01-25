contests = {}
users = {}

while True:
    command = input()
    if command == 'end of submissions':
        break

    if ':' in command:
        while not command == 'end of contests':
            valid_contest, valid_pass = command.split(':')
            contests[valid_contest] = valid_pass
            command = input()

    elif '=>' in command:
        while not command == 'end of submissions':
            curr_contest, curr_pass, username, points = command.split('=>')
            points = int(points)

            for course, passwrd in contests.items():
                if curr_contest == course and curr_pass == passwrd:
                    if username not in users:
                        users[username] = {}

                        if curr_contest not in users[username]:
                            users[username][curr_contest] = points
                            break

                        else:
                            if points > users[username][curr_contest]:
                                users[username][curr_contest] = points
                                break

                    else:

                        if curr_contest not in users[username]:
                            users[username][curr_contest] = points
                            break

                        if points > users[username][curr_contest]:
                            users[username][curr_contest] = points
                            break
            break

max_points = {}
for name, values in sorted(users.items(), key=lambda x: x[0]):
    for k, v in sorted(values.items(), key=lambda x: (-x[1], x[0])):
        if name not in max_points:
            max_points[name] = 0
        max_points[name] += v

max_value = 0
for k, v in max_points.items():
    if v > max_value:
        max_value = v
# print(f'{max(max_points)}, {max_value}')
print(f'Best candidate is {max(max_points)} with total {max_value} points.')
print('Ranking:')

for name, values in sorted(users.items(), key=lambda x: x[0]):

    print(f"{name}")
    for k, v in sorted(values.items(), key=lambda x: -x[1]):
        print(f"#  {k} -> {v}")




























# print(f'{max(max_points)}, {max_points}')
# print(f'Best candidate is {max(max_points)} with total {max_points[1]} points.')

    # print(f'Best candidate is {k} with total {max(v)} points.')

        # print(f"Best candidate is {name} with total {sum(v)} points.")
        # print(f'{name}: {k}, {v}')

    # print(f'{name}')
    # for contest1, points1 in value.items():
    #     print(f'{contest1} -> {points1}')

# {'Tanya': {'C# Fundamentals': 350, 'Algorithms': 380, 'Part One Interview': 220, 'Js Fundamentals': 400}, 'Nikola': {'Part One Interview': 120, 'C# Fundamentals': 200}}
# print(f'"Best candidate is {user} with total {total points} points.".')
# for k, v in sorted(users.items(), key=lambda x: )

