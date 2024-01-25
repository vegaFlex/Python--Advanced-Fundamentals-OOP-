houses = [int(x) for x in input().split('@')]

curr_index = 0
command = input()

while command != 'Love!':
    for house in houses:
        if house == 0:
            print(f"Place {curr_index} has Valentine's day.")


    if houses[curr_index] == 0:
        print(f"Place {curr_index} already had Valentine's day.")

    command_info = command.split()
    length = int(command_info[1])

    if length > len(houses):
        curr_index = 0

    curr_index += length
    houses[curr_index] -= 2

    command = input()
