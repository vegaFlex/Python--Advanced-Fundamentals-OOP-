numbers = [int(x) for x in input().split()]
                                                                # sum_num = sum(numbers)
                                                                # num_count = len(numbers)
                                                                # avg_num = sum_num / num_count
avg_num = sum(numbers) // len(numbers)

larger_numbers = []

for el in numbers:
    if el > avg_num:
        larger_numbers.append(el)
        larger_numbers.sort(reverse=True)

if len(larger_numbers) == 0:
    print('No')
else:
    print(*larger_numbers[:5])


