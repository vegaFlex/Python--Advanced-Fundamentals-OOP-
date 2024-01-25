electrons = int(input())
shell_position = 1

new_list = []
while electrons > 0:
    curr_layer_electron = 2 * pow(shell_position, 2)

    if electrons >= curr_layer_electron:
        new_list.append(curr_layer_electron)

    else:
        new_list.append(electrons)

    electrons -= curr_layer_electron
    shell_position += 1


print(new_list)