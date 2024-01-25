targets = [int(x) for x in input().split(' ')]

while True:
    command = input().split(' ')
    action = command[0]

    if action == "End":
        targets = [str(x) for x in targets]
        print("|".join(targets))
        break

    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value

            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        start = index - value
        end = index + value

        if start >= 0 and end < len(targets):
            del targets[start: end + 1]
        else:
            print("Strike missed!")


