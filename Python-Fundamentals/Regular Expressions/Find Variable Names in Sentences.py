import re

text = input()
# pattern = r"(^_|(?<=\s_))[A-Za-z]+(?=\b)" valid
pattern = r"\b\_(?P<variable_name>[A-Za-z0-9]+)\b"

valid_variables = []
matches = re.finditer(pattern, text)

for match in matches:
    valid_variables.append(match.group('variable_name'))

print(','.join(valid_variables))


