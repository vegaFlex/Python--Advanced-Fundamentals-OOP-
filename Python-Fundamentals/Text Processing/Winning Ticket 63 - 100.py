line = input().split(', ')
valid_symbols = ['@', '#', '$', '^']
valid_ticket = 20

for curr_ticket in line:
    curr_ticket = curr_ticket.strip()

    if len(curr_ticket) == 20:
        half_position = int(len(curr_ticket) / 2)

        left_side = curr_ticket[:half_position]
        right_side = curr_ticket[half_position:]

        left_symbols = ''.join([symbol for symbol in left_side if symbol in valid_symbols])
        right_symbols = ''.join([symbol for symbol in right_side if symbol in valid_symbols])

        if 6 <= len(left_symbols) < 10 and 6 <= len(right_symbols) < 10:
            print(f'ticket "{curr_ticket}" - {len(left_symbols)}{left_symbols[0]}')

        elif len(left_symbols) == 10:
            print(f'ticket "{curr_ticket}" - {len(left_symbols)}{left_symbols[0]} Jackpot!')

        else:
            print(f'ticket "{curr_ticket}" - no match')

    else:
        print("invalid ticket")

