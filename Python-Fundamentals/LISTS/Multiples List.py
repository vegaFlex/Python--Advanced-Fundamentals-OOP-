factor = int(input())
count = int(input())

numbers = []

end_numbers = factor * count
for i in range(factor, end_numbers + 1, factor):
    numbers.append(i)

print(numbers)

