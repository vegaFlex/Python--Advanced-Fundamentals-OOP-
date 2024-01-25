import re

text = input()
matches = []
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

for match in re.finditer(pattern, text):
    matches.append([match.group(2), match.group(3)])

mirror_words = []
for item in matches:
    if item[0] == item[1][::-1]:
        mirror_words.append(f'{item[0]} <=> {item[1]}')

if not matches:
    print("No word pairs found!")
if not mirror_words:
    if matches:
        print(f"{len(matches)} word pairs found!")
    print('No mirror words!')
else:
    print(f'{len(matches)} word pairs found!')
    print('The mirror words are:')
    print(', '.join(mirror_words))
