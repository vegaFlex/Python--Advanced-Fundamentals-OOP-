wagons_cnt = int(input())
wagons = [0] * wagons_cnt

command = input()

while command != 'End':
    command = command.split()
    index = int(command[1])
    if command[0] == 'add':
        wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        wagons[index] += int(command[2])
    elif command[0] == 'leave':
        wagons[index] -= int(command[2])

    command = input()

print(wagons)

