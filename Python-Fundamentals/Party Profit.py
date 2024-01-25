
group_size = int(input())
days = int(input())
total_coins = 0

for day in range(1,days+1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    total_coins += 50 - (group_size * 2)

    if day % 3 == 0:
        total_coins -= group_size * 3

    if day % 5 == 0:
        total_coins += group_size * 20

        if day % 3 == 0:
            total_coins -= group_size * 2

diff = int(total_coins / group_size)
print(f"{group_size} companions received {diff} coins each.")





