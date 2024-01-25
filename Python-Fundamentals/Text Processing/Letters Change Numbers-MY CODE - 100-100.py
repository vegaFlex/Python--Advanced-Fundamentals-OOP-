line = input().split()
final_results = []

for string in line:
    chars = []
    curr_number = ''
    curr_total_sum = 0

    for char in string:
        if char.isalpha():
            chars.append(char)
        elif char.isdigit():
            curr_number += char

    first_chr = chars[0]
    end_chr = chars[1]

    if first_chr.isupper():
        curr_total_sum += int(curr_number) / (ord(first_chr.lower()) - 96)

        if end_chr.isupper():
            curr_total_sum -= (ord(end_chr.lower()) - 96)
        elif end_chr.islower():
            curr_total_sum += ord(end_chr.lower()) - 96

    elif first_chr.islower():
        curr_total_sum += int(curr_number) * (ord(first_chr.lower()) - 96)

        if end_chr.isupper():
            curr_total_sum -= (ord(end_chr.lower()) - 96)
        elif end_chr.islower():
            curr_total_sum += (ord(end_chr.lower()) - 96)

    final_results.append(curr_total_sum)
print(f'{sum(final_results):.2f}')






