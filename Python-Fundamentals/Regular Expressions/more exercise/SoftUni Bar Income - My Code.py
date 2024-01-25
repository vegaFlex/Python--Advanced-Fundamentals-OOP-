import re

pattern = r"%(?P<Name>[A-Z][a-z]+)%([^\|\$\%\.]*?)<(?P<Product>(\w+))>([^\|\$\%\.]*?)(\|(?P<Count>(\d+))\|)[^\|\$\%\.]*?(?P<Price>\d+(.*\d+)*)\$"

total_sum = 0

while True:
    command = input()

    if command == "end of shift":
        break

    matches = re.match(pattern, command)

    if matches:
        name = matches.group('Name')
        product = matches.group('Product')
        count = int(matches.group('Count'))
        price = float(matches.group('Price'))

        total_sum += count * price
        print(f"{name}: {product} - {count * price:.2f}")

print(f'Total income: {total_sum:.2f}')



