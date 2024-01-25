people = int(input())
wagons = list(map(int, input().split()))
free_seats = 0
max_people = 4

for i in range(len(wagons)):
    if wagons[i] > max_people:
        continue
    else:
        waiting_people = abs(wagons[i] - max_people)
        if people < max_people:
            free_seats = max_people - people
            wagons[i] += people
            people -= people
            break

        wagons[i] += waiting_people
        people -= waiting_people
        free_seats += abs(max_people - wagons[i])

if people == 0 and free_seats > 0:
    print(f"The lift has empty spots!")
    print(' '.join(map(str, wagons)))

elif people > 0 and free_seats == 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(map(str, wagons)))

elif free_seats == 0 and people == 0:
    print(' '.join(map(str, wagons)))

