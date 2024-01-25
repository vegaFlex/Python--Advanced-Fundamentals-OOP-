user_name = input().split(", ")

valid_usernames = []

for name in user_name:
    stripped_name = name.strip()
    if 16 > len(name) > 3:
        if name == stripped_name:
            if name.isidentifier() or "-" in name:
                valid_usernames.append(name)
                print(name)



