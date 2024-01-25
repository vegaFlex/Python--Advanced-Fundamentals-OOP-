# 50/100 judge

line = input()
explosion = 0
lenght = 0

for i in range(len(line)):

    if lenght < len(line):
        x = len(line)
        if line[i] == '>':
            if line[i + 1].isdigit():
                explosion += int(line[i + 1])

        for j in range(explosion):
            if line[i + 1] != '>':
                line = line[:i + 1] + line[i + 2:]
                explosion -= 1
            else:
                break
        lenght += 1

print(line)

# 50/100 judge
