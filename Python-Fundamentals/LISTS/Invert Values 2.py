number_str = input().split()

inverted_list = []

for number in number_str:
    inverted_num = int(number) * -1
    inverted_list.append(inverted_num)

print(inverted_list)
