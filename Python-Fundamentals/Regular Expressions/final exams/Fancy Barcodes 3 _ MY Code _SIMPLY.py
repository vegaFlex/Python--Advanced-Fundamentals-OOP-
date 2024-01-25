import re

n = int(input())
pattern = r"(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})"

for i in range(n):
    text = input()
    matches = re.match(pattern, text)

    if matches:
        word = matches.group(2)
        pattern_2 = r"\d"
        num_match = re.findall(pattern_2, word)

        if num_match:
            print(f"Product group: {''.join(num_match)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
