houses = list(map(int, input().split('@')))
length_neighborhood = len(houses)
curr_house = 0

while True:
    command = input()
    if command == 'Love!':
        break

    command_info = command.split()
    jump_length = int(command_info[1])

    curr_house += jump_length

    if curr_house >= length_neighborhood:
        curr_house = 0

    if houses[curr_house] == 0:
        print(f"Place {curr_house} already had Valentine's day.")
    else:
        houses[curr_house] -= 2
        if houses[curr_house] == 0:
            print(f"Place {curr_house} has Valentine's day.")

print(f"Cupid's last position was {curr_house}.")
count = 0

for curr_house in range(len(houses)):
    if houses[curr_house] > 0:
        count += 1

if count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")

