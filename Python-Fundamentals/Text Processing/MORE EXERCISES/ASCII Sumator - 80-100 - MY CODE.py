first_symbol = input()
second_symbol = input()
string = input()

sum_chars = 0
for char in string:
    if ord(char) in range(ord(first_symbol), ord(second_symbol)):
        sum_chars += (ord(char))

print(sum_chars)

