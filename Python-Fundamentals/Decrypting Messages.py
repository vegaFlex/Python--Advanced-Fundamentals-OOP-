key = int(input())
number = int(input())

for i in range(number):
    symbol = input()
    word = key + (ord(symbol))
    total_word = chr(word)
    print(f"{total_word}",end="")


