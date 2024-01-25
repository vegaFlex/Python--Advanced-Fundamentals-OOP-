import re

n = int(input())
pattern = r"(@(#{1,}))([A-Z][A-Za-z0-9]{4,}[A-Z])(@(#){1,})"

for i in range(n):
    text = input()
    matches = re.match(pattern, text)

    if matches:
        word = matches.group()

        pattern_2 = r"(\d)"
        match_num = [match.group() for match in re.finditer(pattern_2, word)]

        if match_num:
            print(f"Product group: {''.join(match_num)}")
        else:
            print('Product group: 00')

    if not matches:
        print('Invalid barcode')
