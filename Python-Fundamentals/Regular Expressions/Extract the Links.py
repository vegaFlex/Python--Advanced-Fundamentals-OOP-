import re

pattern = r"www\.[A-Za-z0-9\-]+(\.[a-z]+)+"
valid_url = []

text = input()
while text != "":
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_url.append(match.group())
    text = input()

[print(url)for url in valid_url]

