num1 = int(input())
num2 = int(input())

a = num1
b = num2
print("Before:")
print(f"a = {a}")
print(f"b = {b}")
c = a
a = b
b = a
print("After:")
print(f"a = {b}")
print(f"b = {c}")

