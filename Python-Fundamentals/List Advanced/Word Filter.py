text = input().split()

result = [el for el in text if len(el) % 2 == 0]

print('\n'.join(result))
