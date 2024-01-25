quantity = int(input())
days_left = int(input())

total_sum = 0
total_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for curr_day in range(1, days_left + 1):
    if curr_day % 11 == 0:
        quantity += 2
    if curr_day % 2 == 0:
        total_sum += ornament_set * quantity
        total_spirit += 5
    if curr_day % 3 == 0:
        total_sum += (tree_skirt + tree_garlands) * quantity
        total_spirit += 13
    if curr_day % 5 == 0:
        total_sum += tree_lights * quantity
        total_spirit += 17
        if curr_day % 3 == 0:
            total_spirit += 30
    if curr_day % 10 == 0:
        total_spirit -= 20
        total_sum += tree_skirt + tree_garlands + tree_lights
if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")






