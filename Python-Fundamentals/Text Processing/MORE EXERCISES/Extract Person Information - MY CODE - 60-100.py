n = int(input())

for i in range(n):
    name = ''
    age = ''
    text = input().split()

    for word in text:
        if '@' and '|' in word:

            start_idx = word.index('@')
            end_idx = word.index('|')

            curr_word = word[start_idx + 1: end_idx]
            name = curr_word

        elif '#' and '*' in word:
            start_idx1 = word.index('#')
            end_idx1 = word.index('*')

            curr_word1 = word[start_idx1 + 1: end_idx1]
            age = curr_word1

    if not name == "" and not age == '':
        print(f"{name} is {age} years old.")






