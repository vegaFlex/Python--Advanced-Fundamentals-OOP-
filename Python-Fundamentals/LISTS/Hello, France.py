items = input().split("|")     # items to buy
budged = int(input())
profit = 0
profit_price_list = []
profit_list = []
profit_price = 0
for index in items:
    profit = 0
    profit_price = 0
    separator = index.split("->")
    if separator[0] == "Clothes":
        if not 0 < float(separator[1]) <= 50:
            continue
    elif separator[0] == "Shoes":
        if not 0 < float(separator[1]) <= 35:
            continue
    elif separator[0] == "Accessories":
        if not 0 < float(separator[1]) <= 20.50:
            continue
    budged -= float(separator[1])       # calculating budged left
    profit_price += float(separator[1]) * 1.40      # calculating the price with 40% increase
    profit += float(separator[1]) * 0.40        # profit = round(profit, 2)       # calculating the profit after the 40% increase for each item
    profit_price_list.append(round(profit_price, 2))    # list with the increased prices
    profit_list.append(profit)      # list with every items' profit
    if budged <= 0:
        budged += float(separator[1])
        profit_price_list.pop()
        profit_list.pop()
        continue

profit_price = sum(profit_list)
price_after_40 = sum(profit_price_list)
budged += price_after_40
print(*profit_price_list)
print(f"Profit: {profit_price:.2f}")
print(); print()
if budged >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
