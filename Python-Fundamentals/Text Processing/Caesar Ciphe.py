text = input()
new_text = ''

for char in text:
    char = ord(char)+3
    new_chr = chr(char)
    new_text += new_chr

print(new_text)