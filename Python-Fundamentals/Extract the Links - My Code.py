import re

pattern = r"w{3}\.[A-Za-z0-9]+[\-A-Za-z0-9]*\.[\.A-Za-z]+"
text = input()

while text != '':
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group())
    text = input()