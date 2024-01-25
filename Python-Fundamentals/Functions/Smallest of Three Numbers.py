def min_num(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        smallest = n1
    elif n2 <= n1 and n2 <= n3:
        smallest = n2
    else:
        smallest = n3
    return smallest


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(min_num(num1, num2, num3))

