command = input()
products = {}

while not command == 'buy':
    product, price, quantity = command.split()
    if product not in products:

        products[product] = []
        products[product].append(float(price))
        products[product].append(int(quantity))
    else:
        values = products.get(product)
        if values[0] != float(price):
            values[0] = float(price)
        values[1] += int(quantity)
    command = input()

for key, value in products.items():
    print(f"{key} -> {value[1] * value[0]:.2f}")




