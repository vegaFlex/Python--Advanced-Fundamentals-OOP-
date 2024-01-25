dwarfs = {}
colors = {}
command = input()

while not command == "Once upon a time":
    name, hatColor, physics = command.split(' <:> ')
    physics = int(physics)
    name = f"{name}:{hatColor}"

    if name not in dwarfs:
        dwarfs[name] = [hatColor, physics]
        if hatColor not in colors:
            colors[hatColor] = 1
        else:
            colors[hatColor] += 1
    else:
        if dwarfs[name][1] < physics:
            dwarfs[name][1] = physics

    command = input()

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][1], colors[x[1][0]]), reverse=True))

for id, v in sorted_dwarfs.items():
    name1, color1 = id.split(':')
    print(f'({color1}) {name1} <-> {v[1]}')
