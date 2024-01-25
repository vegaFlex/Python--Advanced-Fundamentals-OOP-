import re

pattern = r"^>>(?P<Name>[A-Za-z]+)<<(?P<Price>\d+\.?\d+)\!(?P<Qnty>\d+\b)"
furniture = []
total_price = 0

text = input()
while text != 'Purchase':
    match = re.match(pattern, text)

    if match is not None:
        name = match.group('Name')
        price = float(match.group('Price'))
        qnty = int(match.group('Qnty'))

        furniture.append(name)
        total_price += price * qnty

    text = input()
print('Bought furniture:')

for element in furniture:
    print(element)

print(f'Total money spend: {total_price:.2f}')


