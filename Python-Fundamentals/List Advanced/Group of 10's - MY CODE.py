list_nums = [int(x) for x in input().split(', ')]
bounder = 10

while list_nums:
    new_list = []
    for number in list_nums:
        if number in range(bounder - 10, bounder + 1):
            new_list.append(number)

    for number in new_list:
        list_nums.remove(number)
    print(f"Group of {bounder}'s: {new_list}")
    bounder += 10
