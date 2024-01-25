import re

pattern = r"(?P<Day>\d{2})(?P<Sep>[-\./])(?P<Month>[A-Z][a-z]{2})(?P=Sep)(?P<Year>\d{4})"

input_data = input()

matches = re.finditer(pattern, input_data)

for date in matches:
    curr_date = date.groupdict()
    print(f"Day: {curr_date['Day']}, Month: {curr_date['Month']}, Year: {curr_date['Year']}")

