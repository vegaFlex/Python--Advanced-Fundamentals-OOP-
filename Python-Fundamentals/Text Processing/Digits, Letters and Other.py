text = input()
digits = ''
letters = ''
others = ''

for chr in text:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        letters += chr
    else:
        others += chr

print(digits)
print(letters)
print(others)

