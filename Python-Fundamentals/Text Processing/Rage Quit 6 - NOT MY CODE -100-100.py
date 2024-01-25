text = input().upper()
med = ''
final = ''
i = 0

while i < len(text):
    if text[i].isdigit():
        if i < len(text) - 1:
            if text[i + 1].isdigit():
                final += (med * int(str(text[i]) + str(text[i + 1])))
                i += 1
            else:
                final += (med * int(text[i]))
        else:
            final += (med * int(text[i]))
        med = ''
    else:
        med += text[i]
    i += 1

symbols = len(set(final))
print(f"Unique symbols used: {symbols}\n{final}")
