def calculate_total(prod, quant):
    if product == 'coffee':
        return 1.50 * quant
    elif product == 'water':
        return 1.00 * quant
    elif product == 'coke':
        return 1.40 * quant
    elif product == 'snacks':
        return 2.00 * quant


product = input()
quantity = int(input())
a = calculate_total(product, quantity)
print(f"{a:.2f}")
