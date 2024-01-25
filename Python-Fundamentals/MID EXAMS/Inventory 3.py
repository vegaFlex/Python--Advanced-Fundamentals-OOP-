def is_item_exist(el, elements):
    if el in elements:
        return True
    else:
        return False


items = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break

    action = command[0]
    item = command[1]
    is_exist = is_item_exist(item, items)

    if action == 'Collect' and not is_exist:
        items.append(item)

    elif action == 'Drop' and is_exist:
        items.remove(item)

    elif action == 'Combine Items':
        old_item = item.split(':')[0]
        new_item = item.split(':')[1]
        is_exist = is_item_exist(old_item, items)

        if is_exist:
            index = items.index(old_item)
            items.insert(index+1, new_item)

    elif action == 'Renew':
        if is_exist:
            items.remove(item)
            items.append(item)

print(', '.join(items))
