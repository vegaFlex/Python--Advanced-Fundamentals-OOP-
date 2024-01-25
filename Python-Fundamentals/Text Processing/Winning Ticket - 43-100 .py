line = input().split(', ')
valid_symbols = ['@', '#', '$', '^']
valid_ticket = 20

for curr_ticket in line:
    curr_ticket = curr_ticket.strip()

    if len(curr_ticket) == 20:
        half_position = int(len(curr_ticket) / 2)

        left_side = curr_ticket[:half_position]
        right_side = curr_ticket[half_position:]

        left_symbols = ''
        for i in range(len(left_side)):
            if i < (len(left_side) - 1):
                left_cur_i = left_side[i]
                next1 = left_side[i + 1]

                if left_side[i] == left_side[i + 1]:
                    left_symbols += left_side[i]
                else:
                    if left_side[i] == left_side[i - 1]:
                        left_symbols += left_side[i]

            else:
                if left_side[i] == left_side[i - 1]:
                    left_symbols += left_side[i]

        right_symbols = ''
        for i in range(len(right_side)):
            if i < (len(right_side) - 1):
                right_cur_i = right_side[i]
                next2 = right_side[i + 1]

                if right_side[i] == right_side[i + 1]:
                    right_symbols += right_side[i]
                else:
                    if right_side[i] == right_side[i - 1]:
                        right_symbols += right_side[i]
            else:
                if right_side[i] == right_side[i - 1]:
                    right_symbols += right_side[i]

        if len(left_symbols) < len(right_symbols):
            shorter = left_symbols
            longer = right_symbols
        else:
            shorter = right_symbols
            longer = left_symbols

        if 6 <= len(left_symbols) < 10 and 6 <= len(right_symbols) < 10:
            print(f'ticket "{curr_ticket}" - {len(shorter)}{left_symbols[0]}')

        elif len(left_symbols) == 10:
            print(f'ticket "{curr_ticket}" - {len(shorter)}{left_symbols[0]} Jackpot!')

        else:
            print(f'ticket "{curr_ticket}" - no match')

    else:
        print("invalid ticket")
