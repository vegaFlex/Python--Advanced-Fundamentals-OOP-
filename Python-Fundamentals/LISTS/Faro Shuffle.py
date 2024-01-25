cards = input().split()
shuffles_count = int(input())

half_size = len(cards) // 2

for i in range(shuffles_count):
    left_part = cards[0:half_size]
    right_part = cards[half_size:]

    faro_cards = []

    for j in range(len(left_part)):
        faro_cards.append(left_part[j])
        faro_cards.append(right_part[j])

    cards = faro_cards

print(cards)

