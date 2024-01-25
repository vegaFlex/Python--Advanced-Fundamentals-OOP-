line = input()
encrypted = ''

for char in line:
    encrypted += chr(ord(char)+3)

print(encrypted)
