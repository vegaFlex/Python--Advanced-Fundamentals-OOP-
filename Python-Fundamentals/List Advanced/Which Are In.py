str1 = input().split(', ')
str2 = input()

new_list = []

for item in str1:
    if item in str2:
        new_list.append(item)
print(new_list)




