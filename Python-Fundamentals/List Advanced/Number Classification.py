numbers = [int(x) for x in input().split(', ')]

positive_num = [str(el) for el in numbers if el >= 0]
negative_num = [str(el) for el in numbers if el < 0]
even_num = [str(el) for el in numbers if el % 2 == 0]
odd_num = [str(el) for el in numbers if el % 2 == 1]

print(f'Positive: {", ".join(positive_num)}')
print(f'Negative: {", ".join(negative_num)}')
print(f'Even: {", ".join(even_num)}')
print(f'Odd: {", ".join(odd_num)}')

