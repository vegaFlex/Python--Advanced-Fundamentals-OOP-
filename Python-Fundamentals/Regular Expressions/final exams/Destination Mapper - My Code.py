import re

pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'

destinations = []
len_all_symb_in_words = ''
text = input()
for match in re.finditer(pattern, text):
    len_all_symb_in_words += match.group(2)
    destinations.append(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {len(len_all_symb_in_words)}")


