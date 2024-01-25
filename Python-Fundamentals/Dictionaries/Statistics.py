products = {}
command = input()

while command != 'statistics':
    product_name, product_quantity = command.split(': ')
    if product_name not in products:
        products[product_name] = int(product_quantity)
    else:
        products[product_name] += int(product_quantity)
    command = input()

print('Products in stock:')

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")




