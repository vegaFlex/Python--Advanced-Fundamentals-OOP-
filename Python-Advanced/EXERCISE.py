with open('text.txt', 'r') as file:
    for line in file:
        for el in line.split()[::-1]:
            pass