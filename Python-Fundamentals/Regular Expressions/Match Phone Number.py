import re

txt = input()
# pattern = r"\+359(?P<Sep>[\s-])2(?P=Sep)\d{3}(?P=Sep)\d{4}\b" - corect
# pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)" - corect
pattern = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"

matches = re.finditer(pattern, txt)

valid_phones = [match.group() for match in matches]
print(', '.join(valid_phones))
