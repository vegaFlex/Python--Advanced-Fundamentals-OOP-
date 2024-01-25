budget = float(input())
flour_1_kg_price = float(input())

cozonacs_count = 0
colored_egs = 0
left_money = 0

pack_eggs_price = flour_1_kg_price * 0.75
liter_milk = flour_1_kg_price * 1.25
milk_for_cozonac = liter_milk / 4
one_cozonac_price  = flour_1_kg_price + pack_eggs_price + milk_for_cozonac

while budget - one_cozonac_price > 0:
    budget -= one_cozonac_price
    cozonacs_count += 1
    colored_egs += 3
    if cozonacs_count % 3 == 0:
        colored_egs -= cozonacs_count - 2
print(f"You made {cozonacs_count} cozonacs! Now you have {colored_egs} eggs and {budget:.2f}BGN left.")





