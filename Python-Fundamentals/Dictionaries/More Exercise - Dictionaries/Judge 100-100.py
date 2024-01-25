line = input()
contests = {}
all_users = {}

while not line == 'no more time':
    username, contest, points = line.split(' -> ')
    points = int(points)
    if contest not in contests:
        contests[contest] = {username: points}
    else:
        if username in contests[contest]:
            if points > contests[contest][username]:
                contests[contest][username] = points
        else:
            contests[contest][username] = points
    line = input()

for contest, values in contests.items():
    print(f'{contest}: {len(values)} participants')
    position = 1
    for name, point in sorted(values.items(), key=lambda x: (-x[1], x[0])):
        print(f'{position}. {name} <::> {point}')
        position += 1

print('Individual standings:')
for values in contests.values():
    for name, point in values.items():
        if name in all_users.keys():
            all_users[name] += point
        else:
            all_users[name] = point

position = 1
for name, points in sorted(all_users.items(), key=lambda x: (-x[1], x[0])):
    print(f'{position}. {name} -> {points}')
    position += 1

