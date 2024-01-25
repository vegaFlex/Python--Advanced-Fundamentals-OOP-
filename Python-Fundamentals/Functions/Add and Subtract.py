def sum_numbers(n1, n2):
    return n1 + n2


def subtract(sum1, n3):
    return sum1 - n3


def add_and_subtract(n1, n2, n3):
    sum1 = sum_numbers(n1,n2)
    result = subtract(sum1, n3)

    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))

