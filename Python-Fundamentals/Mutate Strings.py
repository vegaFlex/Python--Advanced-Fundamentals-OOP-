first_word = input()
second_word = input()

last_word = first_word

for i in range(len(first_word)):
    left_part = second_word[:i + 1]
    right_part = first_word[i + 1:]
    curr_word = left_part + right_part
    if curr_word == last_word:
        continue
    print(curr_word)
    last_word = curr_word



