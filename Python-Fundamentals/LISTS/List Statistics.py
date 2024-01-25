number = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(number):
    curr_num = int(input())
    if curr_num >= 0:
        positive_numbers.append(curr_num)
    else:
        negative_numbers.append((curr_num))

print(positive_numbers)
print(negative_numbers)

print(f"Count of positives: {len(positive_numbers)}. Sum of negatives: {sum(negative_numbers)}")