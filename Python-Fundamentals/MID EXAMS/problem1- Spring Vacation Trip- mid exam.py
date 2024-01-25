days = int(input())
budget = float(input())
people = int(input())
fuel_per_km = float(input())
food = float(input())
room = float(input())

if people > 10:
    room *= 0.75

expenses = days * people * (food + room)
for i in range(1, days+1):
    travel_distance = float(input())
    expenses += travel_distance * fuel_per_km
    if i % 3 == 0 or i % 5 == 0:
        expenses *= 1.4
    if i % 7 == 0:
        expenses -= expenses / people

    if expenses > budget:
        print(f"Not enough money to continue the trip. You need {(expenses - budget):.2f}$ more. ")
        break
else:
    print(f"You have reached the destination. You have {(budget - expenses):.2f}$ budget left.")
