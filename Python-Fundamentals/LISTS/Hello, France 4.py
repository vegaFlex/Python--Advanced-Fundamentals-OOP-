items = input().split("|")
budget1 = input()
budget = float(budget1)
max_clothes = 50.00
max_shoes = 35.00
max_accessories = 20.50
profit = 0
new_profit = 0
new_price = []
for elements in items:
    if "Clothes" in elements:
        el1 = elements.split('->')
        val = float(el1[1])
        if budget >= val and max_clothes >= val:
            budget -= val
            profit += val * 0.4
            new_price.append(val * 1.4)
            new_profit += val
    elif "Shoes" in elements:
        el1 = elements.split('->')
        val = float(el1[1])
        if budget >= val and max_shoes >= val:
            budget -= val
            profit += val * 0.4
            new_price.append(val * 1.4)
            new_profit += val
    elif "Accessories" in elements:
        el1 = elements.split('->')
        val = float(el1[1])
        if budget >= val and max_accessories >= val:
            budget -= val
            profit += val * 0.4
            new_price.append(val * 1.4)
            new_profit += val

for i in range(len(new_price)):
    print(f"{(new_price[i]):.2f}", end=' ')
print()
print(f'Profit: {profit:.2f}')
if ((new_profit) + budget + (new_profit * 0.4)) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
