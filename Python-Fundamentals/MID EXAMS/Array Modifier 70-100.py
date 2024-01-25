array = [int(x) for x in input().split()]
command = input()

while command != 'end':

    line = command.split()
    action = line[0]

    if action == "decrease":
        for i in range(len(array)):
            array[i] -= 1
        break

    index1 = int(line[1])
    index2 = int(line[2])

    if action == "swap":
        array[index1], array[index2] = array[index2], array[index1]

    elif action == "multiply":
        result = array[index1] * array[index2]
        array[index1] = result

    command = input()

a = (', '.join([str(el) for el in array]))

print(a)
