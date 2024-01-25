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
        if name == dragons[type_d]:
            dragons[type_d] = [name, damage, health, armor]
        else:
            dragons[type_d].append([name, damage, health, armor])

for type1, values in dragons.items():
    values.sort()

new_dict = {}
for type2, values2 in dragons.items():
    if len(values2) == 2:
        a = values2[0][1]
        b = values2[1][1]
        sum_damage = (a + b) / 2

        c = values2[0][2]
        d = values2[1][2]
        sum_health = (c + d) / 2

        e = values2[0][3]
        f = values2[1][3]
        sum_armor = (e + f) / 2

        print(f'{type2}::({sum_damage:.2f}/{sum_health:.2f}/{sum_armor:.2f})')

    elif len(values2) == 1:
        aa = values2[0][1]
        cc = values2[0][2]
        ee = values2[0][3]

        print(f'{type2}::({aa:.2f}/{cc:.2f}/{ee:.2f})')

    for i in values2:
        print(f'-{i[0]} -> damage: {i[1]}, health: {i[2]}, armor: {i[3]}')





