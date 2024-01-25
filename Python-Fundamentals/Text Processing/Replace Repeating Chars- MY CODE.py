text = input()
repeated_symbols = ''

for index in range(len(text)):
    curr_char = text[index]
    if index < len(text)-1:
        if text[index] == text[index + 1]:
            continue
        else:
            repeated_symbols += text[index]
    else:
        repeated_symbols += text[index]
print(repeated_symbols)


