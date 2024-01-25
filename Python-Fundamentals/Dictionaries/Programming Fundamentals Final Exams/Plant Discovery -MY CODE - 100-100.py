n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    rating = []
    plants[plant] = [rarity, rating]

command = input()
while not command == 'Exhibition':
    if 'Rate' in command:
        command1, values1 = command.split(': ')
        plant1, rating1 = values1.split(' - ')
        rating1 = int(rating1)

        if plant1 in plants:
            plants[plant1][1].append(rating1)
        else:
            print('error')

    elif 'Update' in command:
        command1, values1 = command.split(': ')
        plant2, new_rarity2 = values1.split(' - ')
        new_rarity2 = int(new_rarity2)

        if plant2 in plants:
            plants[plant2][0] = new_rarity2
        else:
            print('error')

    elif 'Reset' in command:
        command1, plant3 = command.split(': ')

        if plant3 in plants:
            # plants[plant3] = []
            plants[plant3][1] = []
        else:
            print('error')

    command = input()

print('Plants for the exhibition:')

for curr_plant, curr_values in plants.items():
    if not plants[curr_plant][1]:
        plants[curr_plant][1] = 0
    else:
        plants[curr_plant][1] = sum(plants[curr_plant][1]) / len(plants[curr_plant][1])

sorted_plants = sorted(plants.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
for name, value in sorted_plants:
    print(f"- {name}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
