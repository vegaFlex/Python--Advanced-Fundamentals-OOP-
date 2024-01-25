coffees = input().split()
command = int(input())

for i in range(command):
    curr_command = input().split()

    action = curr_command[0]
    if action == 'Reverse':
        coffees.reverse()

    if action == 'Include':
        coffee_kind = curr_command[1]
        coffees.append(coffee_kind)

    elif action == 'Remove':
        curr_action = curr_command[1]
        index = int(curr_command[2])

        if 0 <= index < len(coffees):
            if curr_action == 'first':
                del coffees[:index]

            elif curr_action == 'last':
                y = len(coffees) - index
                del coffees[y:]

    elif action == "Prefer":
        index1 = int(curr_command[1])
        index2 = int(curr_command[2])
        if 0 <= index1 <= len(coffees) and 0 <= index2 <= len(coffees):
            coffees[index1], coffees[index2] = coffees[index2], coffees[index1]

z = ' '.join([str(el) for el in coffees])
print(f"Coffees: \n"
      f"{z}")
