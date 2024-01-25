students_dict = {}
command = input()

while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name

    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')


# input:
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals