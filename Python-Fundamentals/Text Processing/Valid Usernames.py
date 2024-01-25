line = input().split(', ')

for word in line:
    # if 2 < len(word) < 17 and '-' in word and '_' in word and word.isalnum():
    if 2 < len(word) < 17 and word.isalnum():
        print(word)
    elif 2 < len(word) < 17 and '-' in word:
        print(word)
    elif 2 < len(word) < 17 and '_' in word:
        print(word)

