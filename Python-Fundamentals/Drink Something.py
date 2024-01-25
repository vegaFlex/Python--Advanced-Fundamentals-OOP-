age = int(input())
output = ''

if age <= 14:
    output = 'toddy'
elif age <= 18:
    output = 'coke'
elif age <= 21:
    output = 'beer'
else:
    output = 'whisky'

print(f"drink {output}")

