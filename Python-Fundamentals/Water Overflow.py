tank_capacity = 255
curr_liters_tank = 0
n = int(input())

for i in range(1,n + 1):
    liters_water = int(input())

    if liters_water > tank_capacity:
        print("Insufficient capacity!")
        continue

    tank_capacity -= liters_water
    curr_liters_tank += liters_water

print(curr_liters_tank)





