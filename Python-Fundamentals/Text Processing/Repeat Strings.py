text = input().split()
result = ""
for word in text:
    word *= len(word)
    result += word

print(f'{result}')


