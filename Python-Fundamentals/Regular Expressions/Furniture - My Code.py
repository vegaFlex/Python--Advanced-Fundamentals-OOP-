import re

pattern = r">>(?P<Name>[A-Za-z]+)<<(?P<Price>\d+[.\d+]*)!(?P<Quantity>\d+)"
line = input()

total_furnitutre = []
total_sum = 0
while line != "Purchase":
    matches = re.match(pattern, line)

    if matches is not None:
        name = matches.group('Name')
        price = float(matches.group('Price'))
        qnty = int(matches.group('Quantity'))

        total_sum += price * qnty
        total_furnitutre.append(name)
    line = input()

print('Bought furniture:')
for el in total_furnitutre:
    print(el, end='\n')
print(f'Total money spend: {total_sum:.2f}')