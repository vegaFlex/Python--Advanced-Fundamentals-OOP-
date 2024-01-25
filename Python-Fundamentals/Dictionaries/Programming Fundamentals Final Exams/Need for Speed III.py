n = int(input())
cars = {}
for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

command = input()
while not command == 'Stop':
    if 'Drive' in command:
        command1, car1, distance1, fuel1 = command.split(' : ')
        distance1 = int(distance1)
        fuel1 = int(fuel1)

        if cars[car1][1] < fuel1:
            print('Not enough fuel to make that ride')
        elif cars[car1][1] >= fuel1:
            cars[car1][0] += distance1
            cars[car1][1] -= fuel1
            print(f"{car1} driven for {distance1} kilometers. {fuel1} liters of fuel consumed.")

        if cars[car1][0] >= 100000:
            print(f"Time to sell the {car1}!")
            del cars[car1]

    elif 'Refuel' in command:
        command2, car2, fuel2 = command.split(' : ')
        fuel2 = int(fuel2)

        if cars[car2][1] + fuel2 > 75:
            refill = 75 - cars[car2][1]
            cars[car2][1] = 75
            print(f"{car2} refueled with {refill} liters")
        else:
            cars[car2][1] += fuel2
            print(f"{car2} refueled with {fuel2} liters")

    elif 'Revert' in command:
        command3, car3, kilometers3 = command.split(' : ')
        kilometers3 = int(kilometers3)

        cars[car3][0] -= kilometers3
        if cars[car3][0] < 10000:
            cars[car3][0] = 10000
        else:
            print(f"{car3} mileage decreased by {kilometers3} kilometers")

    command = input()

sorted_cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))
for curr_car, values in sorted_cars.items():
    curr_mileage = values[0]
    curr_fuel = values[1]
    print(f"{curr_car} -> Mileage: {curr_mileage} kms, Fuel in the tank: {curr_fuel} lt.")

