people = int(input())

wagons = [int(wagon) for wagon in input().split(" ")]

for i in range(len(wagons)):
    can_load = min(4 - wagons[i], people)
    wagons[i] += can_load
    people -= can_load

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

elif len([wagon for wagon in wagons if wagon < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(wagon) for wagon in wagons]))


