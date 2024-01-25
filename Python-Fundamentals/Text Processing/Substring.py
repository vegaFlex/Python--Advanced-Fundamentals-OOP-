text_one = input()
text_two = input()

while text_one in text_two:
    text_two = text_two.replace(text_one, '')

print(text_two)

