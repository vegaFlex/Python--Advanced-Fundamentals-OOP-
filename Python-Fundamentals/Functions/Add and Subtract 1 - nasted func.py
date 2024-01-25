def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b

    def subtract():
        result = sum_numbers() - c
        return result

    return subtract()


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))

