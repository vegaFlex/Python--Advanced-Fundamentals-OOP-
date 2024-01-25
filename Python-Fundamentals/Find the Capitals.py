# 1 - во решение
string = input()
index_list = []
for i in range(len(string)):
    if string[i].isupper():
        index_list.append(i)
print(index_list)

# 2-ро решение
word = input()
index_list = []
for index, value in enumerate(word):
    if value.isupper():
        index_list.append(index)
print(index_list)

# 3 - то решение
word = input()
index_list = [index for index, character in enumerate(word) if character.isupper()]
print(index_list)
