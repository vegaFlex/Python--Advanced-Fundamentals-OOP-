my_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
item_obtained = ''

while item_obtained == '':
    line = input().split()
    for i in range(0, len(line), 2):
        qty = int(line[i])
        material = line[i+1].lower()

        if material == 'shards' or material == 'fragments' or material == 'motes':

            # if material not in my_dict:
            #     my_dict[material] = 0
            my_dict[material] += qty

            if material == 'shards' and my_dict[material] >= 250:
                item_obtained = 'Shadowmourne'
                print(f"{item_obtained} obtained!")
                my_dict[material] -= 250
                break

            elif material == 'fragments' and my_dict[material] >= 250:
                item_obtained = 'Valanyr'
                print(f"{item_obtained} obtained!")
                my_dict[material] -= 250
                break

            elif material == 'motes' and my_dict[material] >= 250:
                item_obtained = 'Dragonwrath'
                print(f"{item_obtained} obtained!")
                my_dict[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += qty

for (material_name, material_qty) in sorted(my_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f'{material_name}: {material_qty}')

for (junk_material_name, junk_material_qty) in sorted(junk.items(), key=lambda x: x[0]):
    print(f'{junk_material_name}: {junk_material_qty}')