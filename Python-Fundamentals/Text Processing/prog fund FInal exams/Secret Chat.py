line = input()
data = input()

while not data == 'Reveal':
    split_data = data.split(':|:')
    command = split_data[0]

    if 'InsertSpace' in command:
        index = int(split_data[1])

        line = line[:index] + ' ' + line[index:]
        print(line)

    elif 'Reverse' in command:
        substring = split_data[1]

        if substring in line:
            line = line.replace(substring, '', 1)
            line += substring[::-1]
            print(line)
        else:
            print('error')

    elif 'ChangeAll' in command:
        substring1 = split_data[1]
        replacement = split_data[2]

        line = line.replace(substring1, replacement)
        print(line)

    data = input()

print(f'You have a new text message: {line}')





