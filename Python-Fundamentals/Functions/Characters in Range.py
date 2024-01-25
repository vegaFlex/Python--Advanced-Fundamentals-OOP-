def chr_in_range(a, b):
    for i in range(ord(symbol1) + 1, ord(symbol2)):
        print(f"{chr(i)}", end=" ")


symbol1 = input()
symbol2 = input()

chr_in_range(symbol1, symbol2)


