items = input().split('|')
command = input()

while not command == "Yohoho!":
    action = command.split()[0]
    if action == 'Loot':
        curr_list = command.split()
        for item in curr_list[1:]:
            if item not in items:
                items.insert(0, item)
    elif action == 'Drop':
        index = int(command.split()[1])
        if 0 <= index < len(items):

            x = items.pop(index)
            items.append(x)
    elif action == 'Steal':
        count = int(command.split()[1])

        if len(items) < count:
            print(", ".join(items))
            items = []
        else:
            print(", ".join(items[len(items) - count:]))
            items = items[:len(items) - count]
    command = input()

if len(items) == 0:
    print('Failed treasure hunt.')
else:
    sum_profit = sum(len(x) for x in items)
    el_in_items = len(items)
    avg_profit = sum_profit / el_in_items
    print(f"Average treasure gain: {avg_profit:.2f} pirate credits.")

