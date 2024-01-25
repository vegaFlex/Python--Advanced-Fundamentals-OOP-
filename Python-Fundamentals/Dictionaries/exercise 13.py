n = int(input())
dragons = {}
# new_dict = {}

for _ in range(n):
    type_d, name, damage, health, armor = input().split()
    damage = int(damage)
    health = int(health)
    armor = int(armor)

    if damage == 'null':
        damage = 45
    elif health == 'null':
        health = 250
    elif armor == 'null':
        armor = 10

    if type_d not in dragons:
        dragons[type_d] = {name: [damage, health, armor]}
        # new_dict.update({type_d: name})
    else:
        # dragons[type_d].append([name, damage, health, armor])
        if name == dragons[type_d]:
            dragons[type_d] = {name: [damage, health, armor]}
            # new_dict.update({type_d: name})
        else:
            dragons[type_d].update({name: [damage, health, armor]})
            # new_dict.update({type_d: name})

# sorted_dragons = sorted(dragons.items(), key=lambda x: x[1])
# print(sorted_dragons)

# for k, value in dragons.items():
#     b = [str(x) for x in value]
#
#     b.sort(key=lambda x: x[1], reverse=True)
#     print(b)

#     value.sort(key=lambda value: value[0])
#     # sorted_val = sorted(v)
#     # dragons[k] = sorted_val
#
# print(dragons)
# sorted_dragons = sorted(dragons.items(), key=lambda x: x[1][0])
# print(sorted_dragons)
