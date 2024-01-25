number = int(input())
is_prime = True

for curr_num in range(2, number):
    if number % curr_num == 0:
        is_prime = False
        break
if is_prime:
    print(True)
else:
    print(False)


