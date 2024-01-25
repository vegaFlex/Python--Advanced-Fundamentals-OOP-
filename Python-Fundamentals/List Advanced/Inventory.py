items = input().split(", ")
command = input()

while command != "Craft!":
    command_info = command.split(" - ")

    action = command_info[0]
    curr_item = command_info[1]

    if action == "Collect":
        if curr_item in items:
            continue
        else:
            items.append(curr_item)

    elif action == "Drop":
        if curr_item in items:
            items.remove(curr_item)

    elif action == "Combine Items":
        new_action = curr_item.split(":")
        old_item = new_action[0]
        new_item = new_action[1]

        for i in range(len(items)):
            if items[i] == old_item:
                items.insert(i + 1, new_item)

    elif action == "Renew":
        if curr_item in items:
            items.remove(curr_item)

            items.append(curr_item)

    command = input()

print(", ".join(items))
