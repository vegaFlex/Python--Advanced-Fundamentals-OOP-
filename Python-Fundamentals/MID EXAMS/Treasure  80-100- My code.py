initial_loot = input().split('|')
items = initial_loot
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
        if index < 0 or index >= len(items):
            command = input()
            continue
        x = items[index]
        items.pop(index)
        items.append(x)

    elif action == 'Steal':
        need_to_remove = int(command.split()[1])
        if len(items) < need_to_remove:
            for item in items:
                items.remove(item)
        else:
            length = len(items) - need_to_remove
            y = ', '.join([str(el) for el in items[length:]])
            print(y)
            del items[length:]
    command = input()

if len(items) <= 0:
    print('Failed treasure hunt.')
else:
    sum_profit = sum(len(x) for x in items)
    el_in_items = len(items)
    avg_profit = sum_profit / el_in_items
    print(f"Average treasure gain: {avg_profit:.2f} pirate credits.")

