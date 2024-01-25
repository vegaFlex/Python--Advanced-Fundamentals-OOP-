# 100/100 - TRUE
word = input()
my_dict = {}

for chr in word:
    if chr != ' ':

        if chr not in my_dict:
            my_dict[chr] = 0
        my_dict[chr] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")

# ---------------------------
# 0/100 - FALSE
word = input()
my_dict = {}

for chr in word:
    if chr.isalpha():

        if chr not in my_dict:
            my_dict[chr] = 0
        my_dict[chr] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")



