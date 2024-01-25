factor = int(input())
count = int(input())

numbers = []

bounder = factor * count

for num in range(1,bounder + 1):
    if num % factor == 0:
        numbers.append(num)

print(numbers)
