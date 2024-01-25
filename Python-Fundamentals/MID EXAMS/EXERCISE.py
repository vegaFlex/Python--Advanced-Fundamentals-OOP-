list = input().split()
command = input()

while not command == 'END':
    curr_command = command.split()

    if curr_command[0] == 'Change':
        pos1 = curr_command[1]
        pos2 = curr_command[2]

        if pos1 in list:
            index = list.index(pos1)
            list.pop(index)
            list.insert(index, pos2)

    elif curr_command[0] == 'Hide':
        index1 = curr_command[1]
        if index1 in list:
            list.remove(index1)

    elif curr_command[0] == 'Switch':
        indexx1 = curr_command[1]
        indexx2 = curr_command[2]

        if indexx1 and indexx2 in list:
            z = list.index(indexx1)
            y = list.index(indexx2)
            list[z], list[y] = list[y], list[z]

    elif curr_command[0] == 'Insert':
        index3 = int(curr_command[1])
        element = curr_command[2]

        if 0 <= (index3+1) <= len(list):
            list.insert(index3+1, element)

    elif curr_command[0] == 'Reverse':
        list.reverse()

    command = input()
z = ' '.join([str(el) for el in list])
print(z)
