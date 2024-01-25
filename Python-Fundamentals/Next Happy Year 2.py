year = int(input())

while not len(set(str(year))) == len(str(year)):
    year += 1

print(year)
