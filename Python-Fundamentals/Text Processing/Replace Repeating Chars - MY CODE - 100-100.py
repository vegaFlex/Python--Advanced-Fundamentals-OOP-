line = input()
chars = ''

for i in range(len(line)):
    if i+1 < len(line):
        if line[i + 1] != line[i]:
            chars += line[i]
    else:
        chars += line[i]

print(chars)
