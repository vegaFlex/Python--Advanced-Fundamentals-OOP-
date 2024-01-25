n = int(input())

even_num = []
odd_num = []
negative_num = []
positive_num = []

for i in range(n):
    curr_num = int(input())

    if curr_num % 2 == 0:
        even_num.append(curr_num)
    if curr_num % 2 == 1:
        odd_num.append(curr_num)
    if curr_num < 0:
        negative_num.append(curr_num)
    if curr_num >= 0:
        positive_num.append(curr_num)

command = input()

if command == 'even':
    print(even_num)
elif command == 'odd':
    print(odd_num)
elif command == 'negative':
    print(negative_num)
elif command == 'positive':
    print(positive_num)


