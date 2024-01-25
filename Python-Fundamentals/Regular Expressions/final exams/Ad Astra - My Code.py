import re

pattern = r"(?P<PRODUCTS>(?P<Product>(?P<Sep1>#|\|)[A-Za-z\s]+(?P=Sep1))(?P<Dates>\d{2}(?P<Separator>\/)\d{2}(?P=Separator)\d{2})(?P<Calories>(?P<Sep2>#|\|)\d+(?P=Sep2)))"

products = []
text = input()
matches = re.finditer(pattern, text)

for match in matches:
    product = match.group('Product')[1:-1]
    dates = match.group('Dates')
    calories = int(match.group('Calories')[1:-1])

    products.append([product, dates, calories])

total_calor = []
for el in products:
    calor = el[2]

    total_calor.append(calor)

print(f"You have food to last you for: {sum(total_calor) // 2000} days!")
for element in products:
    print(f"Item: {element[0]}, Best before: {element[1]}, Nutrition: {element[2]}")


