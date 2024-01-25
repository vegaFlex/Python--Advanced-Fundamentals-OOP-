employ1 = int(input())
employ2 = int(input())
employ3 = int(input())

people_count = int(input())
serviced_people_per_hour = employ1 + employ2 + employ3
hour = 0

while people_count > 0:
    hour += 1
    if hour % 4 == 0:
        hour += 1
    people_count -= serviced_people_per_hour
print(f"Time needed: {hour}h.")

