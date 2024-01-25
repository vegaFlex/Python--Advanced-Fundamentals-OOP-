import re

while True:
    curr_line = input()
    pattern = r"\d+"
    matches = re.findall(pattern, curr_line)

    if curr_line == "":
        break
    else:
        if matches:
            print(*matches, end=" ")


