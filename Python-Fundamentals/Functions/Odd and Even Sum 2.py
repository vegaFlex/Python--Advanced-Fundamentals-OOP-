def odd_and_even_sum(n):
    even = [int(x) for x in n if int(x) % 2 == 0]
    odd = [int(x) for x in n if int(x) % 2 == 1]
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


number_string = input()
print(odd_and_even_sum(number_string))
