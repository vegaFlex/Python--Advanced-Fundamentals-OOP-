dwarf = {}
colours = {}

while True:
    command = input()
    if command == 'Once upon a time':
        break
    name, hat_colour, physics = command.split(' <:> ')
    physics = int(physics)
    key = f"{name}:{hat_colour}"

    if key not in dwarf:
        dwarf[key] = [hat_colour, physics]
        if hat_colour not in colours:
            colours[hat_colour] = 1
        else:
            colours[hat_colour] += 1
    else:
        if dwarf[key][1] < physics:
            dwarf[key][1] = physics

snowwhite = dict(sorted(dwarf.items(), key=lambda x: [-x[1][1], -colours[x[1][0]]]))

for key, value in snowwhite.items():
    name, colour = key.split(':')
    print(f"({colour}) {name} <-> {value[1]}")