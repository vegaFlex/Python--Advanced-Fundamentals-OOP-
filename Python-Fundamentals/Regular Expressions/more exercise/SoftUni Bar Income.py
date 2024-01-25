import re
global_pattern = r"\%[A-Z][a-z]+\%[^\|\$\%\.]*?\<\w+\>[^\|\$\%\.]*?\|[0-9]+\|[\w\-]*?[0-9.]+[0-9](?=\$)"
result = []

while True:
    get_name = input()
    if get_name == 'end of shift':
        break
    if re.search(global_pattern, get_name):
        match = re.search(global_pattern, get_name)
        name = re.search(r"(?<=%)\w+(?=%)", match.group())
        product = re.search(r"(?<=<)\w+(?=>)", match.group())
        qty = re.search(r"(?<=\|)\d+(?=\|)", match.group())
        last = match.group().split('|')
        price = re.search(r"[\d.]+", last[-1])
        result.append([name.group(), product.group(), int(qty.group()), float(price.group())])

total = sum(list(map(lambda x: x[2]*x[3],result)))
for item in result:
    print(f"{item[0]}: {item[1]} - {(item[2] * item[3]):.2f}")
print(f"Total income: {total:.2f}")


