def palindrome(a):
    for num in numbers:
        if num[0] == num[-1]:
            print(True)
        else:
            print(False)


numbers = input().split(', ')

palindrome(numbers)
