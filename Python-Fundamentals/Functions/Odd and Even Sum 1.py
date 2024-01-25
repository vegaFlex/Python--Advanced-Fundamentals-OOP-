def odd_and_even_sum(n):
    n = list(map(int, n))
    even = sum([int(x) for x in n if int(x) % 2 == 0])
    return f"Odd sum = {sum(n) - even}, Even sum = {even}"


number = input()
print(odd_and_even_sum(number))


