usernames = input().split(', ')

for name in usernames:
    if 3 <= len(name) < 17:
        if name.isidentifier() or '-' in name:
            print(name)