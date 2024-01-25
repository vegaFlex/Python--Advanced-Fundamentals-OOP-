import re

text = input()
pattern = r"((?<=\s)[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*@[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+)+)"

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())