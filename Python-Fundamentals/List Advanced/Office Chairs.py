rooms = int(input())
total_chairs = 0

for i in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    chairs_count = len(chairs)
    visitors = int(command[1])

    if chairs_count < visitors:
        print(f'{visitors - chairs_count} more chairs needed in room {i}')
        total_chairs -= visitors - chairs_count

    elif chairs_count > visitors:
        total_chairs += chairs_count - visitors

if total_chairs >= 0:
    print(f'Game On, {total_chairs} free chairs left')

