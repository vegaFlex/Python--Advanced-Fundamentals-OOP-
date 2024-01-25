import re

text = input().lower()
search_word = input().lower()

pattern = fr"\b{search_word}\b"
matches = len(re.findall(pattern, text))
print(matches)

