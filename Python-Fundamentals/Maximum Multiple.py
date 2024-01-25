divisor = int(input())
bound = int(input())

max = 0
for curr_num in range(divisor+1, bound+1):
    if curr_num % divisor == 0:
        max = curr_num
print(max)



