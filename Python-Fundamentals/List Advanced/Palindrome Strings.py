words = input().split()
special_word = input()

palindrome = [el for el in words if el == el[::-1]]

print(palindrome)
print(f"Found palindrome {palindrome.count(special_word)} times")

