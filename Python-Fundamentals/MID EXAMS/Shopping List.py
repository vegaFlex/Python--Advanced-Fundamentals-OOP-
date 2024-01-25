def is_item_exist(el, elements):
    elements = set(elements)
    if el in elements:
        return True
    else:
        return False


items = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        break

    action = command.split()[0]
    product = command.split()[1]
    is_exist = is_item_exist(product, items)

    if action == 'Urgent' and not is_exist:
        index = 0
        items.insert(index, product)

    elif action == 'Unnecessary' and is_exist:
        items.remove(product)

    elif action == 'Correct':
        old_item = command.split()[1]
        new_item = command.split()[2]
        is_exist = is_item_exist(old_item, items)

        if is_exist:
            index = items.index(old_item)
            items.pop(index)
            items.insert(index, new_item)

    elif action == 'Rearrange':
        if is_exist:
            index = items.index(product)
            items.pop(index)
            items.append(product)

print(', '.join(items))




