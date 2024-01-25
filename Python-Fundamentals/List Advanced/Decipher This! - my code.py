message = input().split()

for word in message:
    number = ''
    for char in word:
        if char.isdigit():
            number += char

    char_of_ascii = chr(int(number))
    current_word = char_of_ascii + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(''.join(current_word), end=' ')
