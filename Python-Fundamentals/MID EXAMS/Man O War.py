pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input()
lost = False

while not command == 'Retire':
    action = command.split()[0]
    if action == 'Fire':
        index = int(command.split()[1])
        damage = int(command.split()[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                lost = True
                break
    elif action == 'Defend':
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])
        damage1 = int(command.split()[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage1
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
    elif action == 'Repair':
        index2 = int(command.split()[1])
        health = int(command.split()[2])
        if 0 <= index2 < len(pirate_ship):
            if pirate_ship[index2] + health > max_health:
                health = max_health - pirate_ship[index2]
            pirate_ship[index2] += health
    elif action == 'Status':
        below_20_percent = max_health // 5
        count = 0
        for section in pirate_ship:
            if section < below_20_percent:
                count += 1
        print(f'{count} sections need repair.')
    command = input()
if not lost:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')


