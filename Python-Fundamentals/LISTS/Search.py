number = int(input())
word = input()

total_list = []
searched_text = []

for _ in range(number):
    curr_text = input()
    total_list.append(curr_text)
    if word in curr_text:
        searched_text.append(curr_text)

print(total_list)
print(searched_text)

