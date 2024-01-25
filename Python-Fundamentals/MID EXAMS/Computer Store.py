command = input()
price = 0

while not (command == 'special' or command == 'regular'):
    curr_price = float(command)

    if curr_price < 0:
        print('Invalid price!')

    else:
        price += curr_price
    command = input()

taxes = price * 0.20
total_price = price + taxes

if command == 'special':
    total_price *= 0.9

if total_price <= 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print('-----------')
    print(f"Total price: {total_price:.2f}$")




