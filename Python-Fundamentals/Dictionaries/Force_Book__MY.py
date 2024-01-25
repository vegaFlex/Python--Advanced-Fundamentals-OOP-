def force_user_exist(force_book_dict, user):
    for users_list in force_book_dict.values():
        if user in users_list:
            return True

    return False


def remove_user_from_side(force_book_dict, user):
    for (side, users) in force_book_dict.items():
        if user in users:
            force_book_dict[side].remove(user)


def fulfil_conditions_1(force_book_dict, user, side):
    if side not in force_book_dict.keys() and not force_user_exist(force_dict, force_user):
        force_dict[side] = []
        force_dict[side].append(user)

    elif not force_user_exist(force_dict, force_user):
        force_dict[side].append(user)


def fulfil_conditions_2(force_book_dict, user, side):
    if side not in force_book_dict.keys() and not force_user_exist(force_dict, force_user):
        force_dict[side] = []
        force_dict[side].append(user)

    elif not force_user_exist(force_dict, force_user):
        force_dict[side].append(user)

    elif force_user_exist(force_dict, force_user):
        remove_user_from_side(force_dict, force_user)

        if force_side not in force_dict.keys():
            force_dict[force_side] = []
        force_dict[force_side].append(force_user)

    print(f"{force_user} joins the {force_side} side!")


force_dict = {}
command = input()

while not command == "Lumpawaroo":
    if '|' in command:
        data = command.split(' | ')
        force_side = data[0]
        force_user = data[1]

        fulfil_conditions_1(force_dict, force_user, force_side)

    elif '->' in command:
        data = command.split(' -> ')
        force_user = data[0]
        force_side = data[1]

        fulfil_conditions_2(force_dict, force_user, force_side)

    command = input()

for side, users in sorted(force_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')

        for user in sorted(users):
            print(f'! {user}')

