n = int(input())

parking_info = {}

for i in range(n):
    line = input()
    curr_command = line.split()[0]

    if curr_command == 'register':
        username = line.split()[1]
        plate_num = line.split()[2]

        if username not in parking_info:
            parking_info[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")

    elif curr_command == 'unregister':
        username = line.split()[1]

        if username not in parking_info:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_info[username]

[print(f"{k} => {v}")for k, v in parking_info.items()]


