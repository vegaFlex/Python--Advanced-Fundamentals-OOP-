targets = [int(x) for x in input().split()]

shoot_target = 0
curr_target = 0

while True:
    command = input()

    if command == 'End':
        break

    curr_index = int(command)

    if curr_index >= len(targets):
        continue
    if targets[curr_index] == -1:
        continue

    curr_target = targets[curr_index]

    targets[curr_index] = -1
    shoot_target += 1

    for i in range(len(targets)):

        if targets[i] > curr_target and targets[i] != -1:
            targets[i] -= curr_target

        elif targets[i] <= curr_target and targets[i] != -1:
            targets[i] += curr_target

print(f"Shot targets: {shoot_target} -> {' '.join(str(x)for x in targets)}")

