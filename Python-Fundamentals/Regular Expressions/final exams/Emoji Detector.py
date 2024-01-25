import re

pattern_1 = r"(::|\*\*)([A-Z][a-z]{2,})\1"
pattern_2 = r"\d"

cool_treshold = 0
numbers = []
text = input()
matches = re.finditer(pattern_2, text)
for match in matches:
    numbers.append(match.group())

for num in numbers:
    if cool_treshold == 0:
        cool_treshold = int(num)
    else:
        cool_treshold *= int(num)

print(f'Cool threshold: {cool_treshold}')

valid_emojis = []
emoji_match = re.finditer(pattern_1, text)
for match in emoji_match:
    valid_emojis.append(match.group())

print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

for word in valid_emojis:
    word_trimed = word[2:-2]

    word_ascii_sum = 0
    for i in word_trimed:
        word_ascii_sum += ord(i)
    if word_ascii_sum >= cool_treshold:
        print(word)

