import re

patren_leters = r"([A-Za-z])"
patren_numbers = r"\d"

valid_participants = input()
text = input()

racers = {}
while text != 'end of race':
    name = re.findall(patren_leters, text)
    name = ''.join(name)
    numbers = re.findall(patren_numbers, text)

    total_km = 0
    for num in numbers:
        total_km += int(num)

    if name in valid_participants:
        if name not in racers:
            racers[name] = total_km
        else:
            racers[name] += total_km
    text = input()

sorted_racers = dict(sorted(racers.items(), key=lambda x: x[1], reverse=True))

list_racers = []
for key, value in sorted_racers.items():
    list_racers.append([f'{key}'])

counter = 0
for name in list_racers[0:3]:
    counter += 1

    if counter == 1:
        extension = 'st'
    elif counter == 2:
        extension = 'nd'
    elif counter == 3:
        extension = 'rd'

    print(f"{counter}{extension} place: {''.join(name)}")




