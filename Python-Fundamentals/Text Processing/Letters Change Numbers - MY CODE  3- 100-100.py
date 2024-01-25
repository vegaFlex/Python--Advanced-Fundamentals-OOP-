line = input().split()
total_sum = 0

for curr_string in line:
    start_letter = curr_string[0]
    end_letter = curr_string[-1]

    digits = ''
    for chr in curr_string:
        if chr.isdigit():
            digits += chr

    if start_letter.isupper():
        digits = int(digits) / (ord(start_letter.lower()) - 96)

        if end_letter.isupper():
            digits -= (ord(end_letter.lower()) - 96)
        else:
            digits += (ord(end_letter) - 96)

    else:
        digits = int(digits) * (ord(start_letter.lower()) - 96)

        if end_letter.isupper():
            digits -= (ord(end_letter.lower()) - 96)
        else:
            digits += (ord(end_letter) - 96)

    total_sum += float(digits)

print(f'{total_sum:.2f}')




