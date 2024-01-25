energy = int(input())
won_battles = 0

command = input()
while command != 'End of battle':
    needed_distance = int(command)

    if energy < needed_distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    else:
        energy -= needed_distance
        won_battles += 1

        if won_battles % 3 == 0:
            energy += won_battles

    command = input()

if command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {energy}")


