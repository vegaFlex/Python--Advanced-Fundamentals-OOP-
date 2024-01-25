text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [el for el in text if el.lower() not in vowels]
print(''.join(result))





