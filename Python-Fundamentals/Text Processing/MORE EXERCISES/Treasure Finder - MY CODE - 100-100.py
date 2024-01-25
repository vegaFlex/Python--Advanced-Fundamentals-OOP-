numbers = input().split()
command = input()
counter = 0

while not command == 'find':
    curr_text = command
    counter = 0
    new_text = ''

    for i in range(len(curr_text)):
        symb = ''
        num = 0

        symb = curr_text[i]

        while counter < len(numbers):
            num = numbers[counter]
            break
        else:
            counter = 0
            num = numbers[counter]

        counter += 1
        new_symb = ord(symb) - int(num)
        new_text += chr(new_symb)

    type_treasure = ''
    start_index = new_text.index('&')

    for idx in range(start_index+1, len(new_text)):
        curr_char = new_text[idx]
        type_treasure += curr_char
        if new_text[idx+1] == '&':
            break

    coordinates = ''
    start_idx = new_text.index('<')
    end_idx = new_text.index('>')

    for symbol in range(start_idx+1, end_idx):
        coordinates += new_text[symbol]
    print(f"Found {type_treasure} at {coordinates}")

    command = input()













