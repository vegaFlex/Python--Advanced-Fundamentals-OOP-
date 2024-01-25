line = input()
all_dwarfs = {}
colors = {}

while not line == 'Once upon a time':
    name, hatColor, physics = line.split(' <:> ')
    physics = int(physics)
    name = f'{name}:{hatColor}'

    if name not in all_dwarfs:
        all_dwarfs[name] = [hatColor, physics]
        if hatColor not in colors:
            colors[hatColor] = 1
        else:
            colors[hatColor] += 1
    else:
        if all_dwarfs[name][1] < physics:
            all_dwarfs[name][1] = physics

    line = input()

sorted_dict = dict(sorted(all_dwarfs.items(), key=lambda x: [-x[1][1], -colors[x[1][0]]]))

for key, value in sorted_dict.items():
    name, colour = key.split(':')
    print(f"({colour}) {name} <-> {value[1]}")

