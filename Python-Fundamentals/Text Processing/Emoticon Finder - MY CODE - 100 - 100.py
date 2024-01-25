line = input()

for i in range(len(line)):
    x = line[i]
    if x == ':':
        emoticons = x + line[i+1]
        print(emoticons)


