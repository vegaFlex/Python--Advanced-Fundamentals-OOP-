contests = {}
line_one = input()
while not line_one == "end of contests":
    valid_contest, valid_password = line_one.split(":")
    contests[valid_contest] = valid_password
    line_one = input()

users = {}
line_two = input()
while not line_two == "end of submissions":
    contest, password, username, points = line_two.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {contest: points}
        else:
            if contest in users[username]:
                if users[username][contest] < points:
                    users[username][contest] = points
            else:
                users[username][contest] = points
    line_two = input()

max_points = 0
best_candidate = ' '
for user, values in users.items():
    current_points = 0
    for course, point in values.items():
        current_points += point
    if current_points > max_points:
        max_points = current_points
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

for user, value in sorted(users.items(), key=lambda kvp: kvp[0]):
    print(f"{user}")
    for contest, point in sorted(value.items(), key=lambda kvp: -kvp[1]):
        print(f"#  {contest} -> {point}")

