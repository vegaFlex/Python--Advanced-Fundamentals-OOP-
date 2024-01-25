def odd_and_even_sum(a):
    odd_sum = 0
    even_sum = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = int(input())

odd_and_even_sum(number)
