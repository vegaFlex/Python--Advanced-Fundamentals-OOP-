products = input().split("|")
budget = float(input())

element = ''
bought_products = []
profit = []
total_profit = 0

for item in products:
    element = item.split("->")
    wear = element[0]
    price = float(element[1])
    if budget - price >= 0:

        if (wear == "Clothes" and price <= 50.0) \
                or (wear == "Shoes" and price <= 35.0) \
                or (wear == "Accessories" and price <= 20.50):
            bought_products.append(price)
            budget -= price

profitt = 0.4*(sum(bought_products))
for i in range(len(bought_products)):

    print(f"{(bought_products[i]*1.4):.2f}", end=' ')
print()
print(f'Profit: {profitt:.2f}')

total_profit = budget + sum(bought_products) * 1.4

if total_profit >= 150:

    print(f"Hello, France!")
else:

    print("Time to go.")
