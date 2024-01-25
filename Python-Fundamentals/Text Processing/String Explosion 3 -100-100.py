line = input()
explosion = 0
i = 0

while i < len(line):
    if line[i] == '>':
        explosion += int(line[i + 1])
    else:
        if explosion > 0:
            line = line[:i] + line[i + 1:]
            explosion -= 1
            i -= 1

    i += 1

print(line)
