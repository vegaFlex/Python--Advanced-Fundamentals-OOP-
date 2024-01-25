n = int(input())
total_sum = 0
for i in range(n):
    chr = input()
    total_sum += ord(chr)
print(f"The sum equals: {total_sum}")
