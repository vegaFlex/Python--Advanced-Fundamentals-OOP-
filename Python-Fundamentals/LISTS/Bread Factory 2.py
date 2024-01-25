energy = 100
coins = 100
is_bankrupted = False
events = input().split('|')

for event in events:
    event_info = event.split('-')
    curr_event = event_info[0]
    digit = int(event_info[1])

    if curr_event == 'rest':
        energy_gained = digit
        if energy + digit > 100:
            energy_gained = 100 - energy
        energy += energy_gained
        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {energy}.')

    elif curr_event == 'order':
        if energy - 30 >= 0:
            coins += digit
            energy -= 30
            print(f'You earned {digit} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins - digit > 0:
            coins -= digit
            print(f'You bought {curr_event}.')
        else:
            print(f'Closed! Cannot afford {curr_event}.')
            is_bankrupted = True
            break

if not is_bankrupted:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')