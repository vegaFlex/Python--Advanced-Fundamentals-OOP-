line = input().split()
string1 = line[0]
string2 = line[1]

str1 = []
for chr1 in string1:
    str1.append(ord(chr1))

str2 = []
for chr2 in string2:
    str2.append(ord(chr2))

total_sum = 0
longer = []
shorter = []

if len(str1) > len(str2):
    longer = str1
    shorter = str2
else:
    longer = str2
    shorter = str1

for index in range(len(longer)):
    if index in range(len(shorter)):
        total_sum += longer[index] * shorter[index]
    else:
        for posit in range(len(longer)-1, len(shorter)-1, -1):
            total_sum += longer[posit]
        break

print(total_sum)