array = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        print(', '.join(map(str, array)))
        break

    elif command[0] == "decrease":
        array = [x - 1 for x in array]

    elif command[0] == "swap":
        array[int(command[1])], array[int(command[2])] = array[int(command[2])], array[int(command[1])]

    elif command[0] == "multiply":
        array[int(command[1])] *= array[int(command[2])]






