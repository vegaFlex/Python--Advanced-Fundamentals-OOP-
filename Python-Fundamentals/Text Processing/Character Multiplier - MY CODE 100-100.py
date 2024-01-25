line = input().split()

string_1 = line[0]
string_2 = line[1]
total = 0

if len(string_1) > len(string_2):
    longer = string_1
    shorter = string_2
else:
    longer = string_2
    shorter = string_1

for i in range(len(longer)):
    if i in range(len(shorter)):
        total += ord(longer[i]) * ord(shorter[i])
    else:
        total += ord(longer[i])

print(total)
