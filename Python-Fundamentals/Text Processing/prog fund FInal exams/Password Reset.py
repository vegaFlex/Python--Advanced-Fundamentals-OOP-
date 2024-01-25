line = input()

while True:
    split_data = input().split()
    curr_cmnd = split_data[0]

    if curr_cmnd == 'Done':
        print(f'Your password is: {line}')
        break

    if 'TakeOdd' in curr_cmnd:
        new_text = ''
        for i in range(len(line)):
            if i % 2 == 1:
                new_text += line[i]
        line = new_text
        print(new_text)

    elif 'Cut' in curr_cmnd:
        index = int(split_data[1])
        length = int(split_data[2])

        substring = line[index:index+length]
        line = line.replace(substring, '', 1)
        print(line)

    elif 'Substitute' in curr_cmnd:
        substring1 = split_data[1]
        substitute = split_data[2]

        if substring1 in line:
            line = line.replace(substring1, substitute)
            print(line)
        else:
            print('Nothing to replace!')



