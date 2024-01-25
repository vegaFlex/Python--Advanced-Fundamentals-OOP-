
# this code has 28/100 in JUDGE system.

line = input()
symbols = ''
curr_char = ''
unique_chars = 0

for i in range(len(line)):

    if not line[i].isdigit():
        # if line[i].upper() not in symbols:
        curr_char += line[i].upper()
        if line[i].upper() not in symbols:
            unique_chars += 1
    else:
        repeated = int(line[i])
        symbols += curr_char * repeated
        curr_char = ''

print(f'Unique symbols used: {unique_chars}')
print(symbols)

# this code has 28/100 in JUDGE system.