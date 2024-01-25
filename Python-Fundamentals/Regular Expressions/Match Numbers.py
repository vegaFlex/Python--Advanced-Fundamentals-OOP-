import re

input_data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, input_data)

# for match in matches:
#     result = match.group()
#     print(result, end= " ")   - correct

matches = [match.group() for match in matches]
print(*matches)


