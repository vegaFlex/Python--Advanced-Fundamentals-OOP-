year = int(input())

for i in range(len(str(year))):
    check = str(year).count(str(year)[i])

    while check > 1:
        year += 1
        check = str(year).count(str(year)[i])

print(year)
