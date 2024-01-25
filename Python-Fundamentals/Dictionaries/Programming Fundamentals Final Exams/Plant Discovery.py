n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant in plants:
        plants[plant]['RARITY'] += rarity
        plants[plant]['RATING'] = []
    else:
        plants[plant] = {'RARITY': rarity, 'RATING': []}

command = input()
while not command == 'Exhibition':
    if 'Rate' in command:
        curr_command, values = command.split(': ')
        curr_plant, curr_value = values.split(' - ')
        curr_value = int(curr_value)
        if curr_plant in plants:
            plants[curr_plant]['RATING'].append(curr_value)
        else:
            print('error')
    elif 'Update' in command:
        curr_command, values = command.split(': ')
        curr_plant, curr_value = values.split(' - ')
        curr_value = int(curr_value)
        if curr_plant in plants:
            plants[curr_plant]['RARITY'] = curr_value
        else:
            print('error')
    elif 'Reset' in command:
        curr_command, curr_plant = command.split(': ')
        if curr_plant in plants:
            plants[curr_plant]['RATING'] = []
        else:
            print('error')
    command = input()

print('Plants for the exhibition:')
for name, value in plants.items():
    if not plants[name]['RATING']:
        plants[name]['RATING'] = 0
    else:
        plants[name]['RATING'] = sum(plants[name]['RATING']) / len(plants[name]['RATING'])

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['RARITY'], x[1]['RATING']), reverse=True)
for name, value in sorted_plants:
    print(f"- {name}; Rarity: {value['RARITY']}; Rating: {value['RATING']:.2f}")


