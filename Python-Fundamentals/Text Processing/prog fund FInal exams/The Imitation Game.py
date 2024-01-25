line = input()
command = input()

while not command == 'Decode':
    if 'Move' in command:
        num_letter_moves = int(command.split('|')[1])

        line = line[num_letter_moves:] + line[:num_letter_moves]

    elif 'Insert' in command:
        index = int(command.split('|')[1])
        value = command.split('|')[2]

        line = line[:index] + value + line[index:]

    elif 'ChangeAll' in command:
        substring = command.split('|')[1]
        replacement = command.split('|')[2]

        line = line.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {line}')


