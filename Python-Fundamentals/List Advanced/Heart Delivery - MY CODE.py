houses = [int(x) for x in input().split("@")]
house_index = 0
unsuccessful_try = 0

while True:
    command = input()
    if command == "Love!":
        break

    jump_info = command.split()
    length_jump = int(jump_info[1])

    house_index += length_jump

    if house_index >= len(houses):
        house_index = 0

    if houses[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        houses[house_index] -= 2
        if houses[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")

print(f"Cupid's last position was {house_index}.")

for house in houses:
    if house > 0:
        unsuccessful_try += 1

if unsuccessful_try > 0:
    print(f"Cupid has failed {unsuccessful_try} places.")
else:
    print(f"Mission was successful.")

