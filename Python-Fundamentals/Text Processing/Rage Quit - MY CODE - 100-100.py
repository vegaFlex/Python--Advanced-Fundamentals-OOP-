
line = input().upper()
symbols = ''
curr_char = ''

for i in range(len(line)):
    curr_symbol = line[i]
    if not line[i].isdigit():
        curr_char += line[i]
    else:
        repeated = ''
        if i != len(line) - 1:                      # лекарство срещу index out of range
            if line[i + 1].isdigit():               # проверка дали следващият символ е число
                repeated += line[i] + line[i + 1]
            else:
                repeated += line[i]
        else:
            repeated += line[i]

        repeated = int(repeated)
        symbols += curr_char * repeated
        curr_char = ''

print(f'Unique symbols used: {len(set(symbols))}')
print(symbols)




