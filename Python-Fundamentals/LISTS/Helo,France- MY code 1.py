items = input().split('|')
budget = float(input())

profit = 0.00
bought_item = []
new_bought_item = []

for item in items:
    args = item.split('->')
    product = args[0]
    price = float(args[1])

    if (product == 'Clothes' and price <= 50) \
            or (product == 'Shoes' and price <= 35) \
            or (product == 'Accessories' and price <= 20.50):

        if budget < price:
            continue

        budget -= price
        bought_item.append(float(price))

profit = sum(bought_item) * 0.4

for el in bought_item:
    el *= 1.4
    new_bought_item.append(float(el))
    print(f'{el:.2f}', end=" ")

print()
print(f'Profit: {profit:.2f}')

if sum(new_bought_item) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')






