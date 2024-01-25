cities = {}
command_one = input()
while not command_one == 'Sail':
    town, people, gold = command_one.split('||')
    people = int(people)
    gold = int(gold)

    if town not in cities:
        cities[town] = [people, gold]
    else:
        cities[town][0] += people
        cities[town][1] += gold
    command_one = input()

command_two = input()
while not command_two == 'End':
    if 'Plunder' in command_two:
        curr_command1, town1, people1, gold1 = command_two.split('=>')
        people1 = int(people1)
        gold1 = int(gold1)
        cities[town1][0] -= people1
        cities[town1][1] -= gold1
        print(f'{town1} plundered! {gold1} gold stolen, {people1} citizens killed.')

        if cities[town1][0] == 0 or cities[town1][1] == 0:
            print(f'{town1} has been wiped off the map!')
            del cities[town1]

    elif 'Prosper' in command_two:
        curr_command2, town2, gold2 = command_two.split('=>')
        gold2 = int(gold2)
        if gold2 < 0:
            print(f'Gold added cannot be a negative number!')
        elif gold2 > 0:
            cities[town2][1] += gold2
            print(f"{gold2} gold added to the city treasury. {town2} now has {cities[town2][1]} gold.")
    command_two = input()

if not cities == {}:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for town3, values in cities.items():
        peoples = values[0]
        golds = values[1]
        print(f'{town3} -> Population: {peoples} citizens, Gold: {golds} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')

