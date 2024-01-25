def submissions_count(field, temp_dict):
    if field not in temp_dict:
        temp_dict[field] = 1
    else:
        temp_dict[field] += 1


def add_stats(user, points, my_dict):
    if user not in my_dict.keys():
        my_dict[user] = [points]
    else:
        for student, information in my_dict.items():
            if student == user:
                if information[0] < points:
                    information[0] = points
                    break


def banned(user, my_dict):
    my_dict.pop(user)


stats = {}
languages = {}

while True:
    data = input()
    if data == "exam finished":
        break
    else:
        data = data.split("-")
        if "banned" in data:
            name = data[0]
            banned(name, stats)
        else:
            name = data[0]
            language = data[1]
            result = int(data[2])
            add_stats(name, result, stats)
            submissions_count(language, languages)

print('Results:')
[print(f"{key} | {value[0]}") for key, value in sorted(stats.items(), key=lambda kvp: (-kvp[1][0], kvp[0]))]
print("Submissions:")
[print(f"{key} - {value}") for key, value in sorted(languages.items(), key=lambda kvp: (-kvp[1], kvp[0]))]

