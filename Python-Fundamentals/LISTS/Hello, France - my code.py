items = input().split('|')
budget = float(input())

old_items_price = []

for item in items:
    args = item.split('->')
    type = args[0]
    price = float(args[1])

    if type == 'Clothes' and price <= 50 \
            or type == 'Shoes' and price <= 35 \
            or type == 'Accessories' and price <= 20.50:
        if budget < price:
            continue
        budget -= price
        old_items_price.append(price)

profit = 0.4 * (sum(old_items_price))

for i in range(len(old_items_price)):
    print(f"{(old_items_price[i] * 1.4):.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

total_profit = budget + sum(old_items_price) * 1.4

if total_profit >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


