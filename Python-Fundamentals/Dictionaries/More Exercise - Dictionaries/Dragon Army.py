n = int(input())
dragons = {}

for _ in range(n):
    type_d, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    elif health == 'null':
        health = 250
    elif armor == 'null':
        armor = 10
    damage = int(damage)
    health = int(health)
    armor = int(armor)

    if type_d not in dragons:
        dragons[type_d] = []
        dragons[type_d].append([name, damage, health, armor])
    else:
        if name == dragons[type_d][0][0]:
            dragons[type_d] = [name, damage, health, armor]
        else:
            dragons[type_d].append([name, damage, health, armor])

for values in dragons.values():
    values.sort()

new_dict = {}
for type2, values2 in dragons.items():
    sum_damage = 0
    sum_health = 0
    sum_armor = 0
    delimiter = 0

    for i in values2:
        delimiter += 1
        sum_damage += i[1]
        sum_health += i[2]
        sum_armor += i[3]

    new_dict[type2] = [sum_damage / delimiter, sum_health / delimiter, sum_armor / delimiter]

for k, v in new_dict.items():
    print(f'{k}::({v[0]:.2f}/{v[1]:.2f}/{v[2]:.2f})')

    for itr in dragons[k]:
        print(f'-{itr[0]} -> damage: {itr[1]}, health: {itr[2]}, armor: {itr[3]}')








