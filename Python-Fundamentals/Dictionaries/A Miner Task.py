command = input()
my_list = []
my_dict = {}

while not command == "stop":
    curr_command = command
    my_list.append(curr_command)
    command = input()

for i in range(0, len(my_list), 2):
    key = my_list[i]
    value = int(my_list[i+1])

    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += value

for k, v in my_dict.items():
    print(f"{k} -> {v}")


