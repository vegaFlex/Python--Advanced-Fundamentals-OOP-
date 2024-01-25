lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken_count = 0
gladiator_expenses = 0

for lost_game in range(1, lost_fights_count+1):

    if lost_game % 2 == 0:
        gladiator_expenses += helmet_price

    if lost_game % 3 == 0:
        gladiator_expenses += sword_price

    if lost_game % 2 == 0 and lost_game % 3 == 0:
        gladiator_expenses += shield_price
        shield_broken_count += 1

    if shield_broken_count == 2:
        gladiator_expenses += armor_price
        shield_broken_count = 0

print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")

