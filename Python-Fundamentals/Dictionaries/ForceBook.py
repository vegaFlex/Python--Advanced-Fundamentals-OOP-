command = input()
sides = {}
while command != 'Lumpawaroo':
    if '|' in command:
        command_info = command.split(' | ')
        side = command_info[0]
        user = command_info[1]

        if user not in sides and side not in sides:
            sides[side] = []
        sides[side].append(user)

        if user not in sides[side]:
            sides[side].append(user)

    else:
        command_info = command.split(' -> ')
        user = command_info[0]
        side = command_info[1]
        old_side = ""

        for key, value in sides.items():
            if user in value:
                old_side = key
                break

        if old_side != "":
            sides[old_side].remove(user)
            if side not in sides:
                sides[side] = []

            sides[side].append(user)

        else:
            if side not in sides:
                sides[side] = []

            sides[side].append(user)

        print(f"{user} joins the {side} side!")

    command = input()

sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue

    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users):
        print(f"! {user}")