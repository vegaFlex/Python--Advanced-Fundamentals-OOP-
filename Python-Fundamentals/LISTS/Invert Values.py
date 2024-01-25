line = input()
curr_list = line.split()

inverted_list = []

for el in curr_list:
    inverted_num = int(el) * -1
    inverted_list.append(inverted_num)

print(inverted_list)
