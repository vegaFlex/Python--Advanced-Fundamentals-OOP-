import re

text = input()
pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+(?=\b)"

valid_variables = [obj.group()for obj in re.finditer(pattern, text)]
print(*valid_variables, sep=',')


