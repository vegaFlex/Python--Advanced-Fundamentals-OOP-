elements = input().split()
command = input()
moves = 0

while not command == 'end':
    moves += 1

    index1 = int(command.split()[0])
    index2 = int(command.split()[1])

    if ((index1 or index2) < 0) or ((index1 or index2) >= len(elements)) or (index1 == index2):
        middle = int(len(elements)) // 2

        elements.insert(middle, f"-{str(moves)}a")
        elements.insert(middle, f"-{str(moves)}a")
        print('Invalid input! Adding additional elements to the board')

    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        x = elements.pop(index1)
        elements.remove(x)

    elif elements[index1] != elements[index2]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if command == "end":
    print("Sorry you lose :(\n"
          f"{' '.join(elements)}")


