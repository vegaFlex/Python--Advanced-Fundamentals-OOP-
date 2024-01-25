line = input()

new_list = ""
explosion = 0
length = 0

while length < len(line):
    for i in range(len(line)):
        curr_iteration = line[i]

        if line[i] != ">" and explosion > 0:
            explosion -= 1
        elif line[i] == ">":
            explosion += int(line[i + 1])
            new_list += line[i]
        else:
            new_list += line[i]
        length += 1
print(new_list)
