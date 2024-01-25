max_health = 100
curr_health = max_health
rooms = input().split('|')
bitcoins = 0
curr_room = 0
is_dead = False

for i in range(len(rooms)):
    curr_room += 1
    command = rooms[i]
    action = command.split()

    if action[0] == 'potion':
        health = int(action[1])

        if curr_health + health > 100:
            health = max_health - curr_health
            curr_health = max_health
        else:
            curr_health += health
        print(f"You healed for {health} hp.")
        print(f"Current health: {curr_health} hp.")

    elif action[0] == 'chest':
        found_bitcoin = int(action[1])

        bitcoins += found_bitcoin
        print(f"You found {found_bitcoin} bitcoins.")
    else:
        monster = action[0]
        monster_attack = int(action[1])
        curr_health -= monster_attack
        if curr_health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {curr_room}")
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {curr_health}")





