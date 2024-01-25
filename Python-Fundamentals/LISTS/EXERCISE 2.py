items = input().split('|')
budget = float(input())

profit = 0.00

old_buy_item = 0.00
new_buy_item = 0.00
old_items_price = []
new_items_price = []

for item in items:
    args = item.split('->')
    type = args[0]
    price = float(args[1])

    if type == 'Clothes' and price <= 50 \
            or type == 'Shoes' and  price <= 35 \
            or type == 'Accessories' and price <= 20.50:
        if budget < price:
            continue
        budget -= price
        old_buy_item += price
        old_items_price.append(price)


for el in old_items_price:
    el *= 1.4
    new_items_price.append(float(el))
    print(f'{el:.2f}', end=" ")

profit = sum(new_items_price) - sum(old_items_price)
print(sep="\n")
print(f"Profit: {profit:.2f}")

if budget + sum(new_items_price) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")