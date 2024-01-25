targets_list = list(map(int, input().split()))

command = input()

while command != "End":
    split_command, index, value = command.split()
    index = int(index)
    value = int(value)

    if split_command == "Shoot":
        if 0 <= int(index) <= len(targets_list):
            targets_list[index] -= value
            if targets_list[index] <= 0:
                targets_list.pop(index)

    elif split_command == "Add":
        if 0 <= int(index) <= len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")

    elif split_command == "Strike":
        if 0 <= int(index) <= len(targets_list) and int(index)-value >= 0 and int(index)+value <= len(targets_list):
            del targets_list[index - value: (index + value) + 1]
        else:
            print("Strike missed!")

    command = input()

print('|'.join([str(target) for target in targets_list]))
