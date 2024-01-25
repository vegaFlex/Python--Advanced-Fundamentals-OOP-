number = int(input())
word = input()
strings = []

for i in range(number):
    curr_str = input()
    strings.append((curr_str))
print(strings)

for i in range(len(strings) -1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)
