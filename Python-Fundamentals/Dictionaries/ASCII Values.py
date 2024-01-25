list_char = input().split(', ')

# my_dict = {}
# for chr in list_char:
#     chr_to_ascii = ord(chr)
#     my_dict[chr] = chr_to_ascii
# print(my_dict)

my_dict = {chr: ord(chr) for chr in list_char}
print(my_dict)