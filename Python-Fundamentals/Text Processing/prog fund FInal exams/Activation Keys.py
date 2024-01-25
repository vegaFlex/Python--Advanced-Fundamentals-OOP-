activation_key = input()
command = input()

while command != 'Generate':
    split_data = command.split('>>>')
    curr_cmnd = split_data[0]

    if 'Contains' in command:
        substring = split_data[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif 'Flip' in command:
        action = split_data[1]
        start_idx = int(split_data[2])
        end_idx = int(split_data[3])

        text_to_change = activation_key[start_idx:end_idx]

        if action == 'Upper':
            text_to_change = text_to_change.upper()
            activation_key = activation_key[:start_idx] + text_to_change + activation_key[end_idx:]
        elif action == 'Lower':
            text_to_change = text_to_change.lower()
            activation_key = activation_key[:start_idx] + text_to_change + activation_key[end_idx:]

        print(activation_key)

    elif 'Slice' in command:
        start_index = int(split_data[1])
        end_index = int(split_data[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
