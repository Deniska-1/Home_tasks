# Задача 2.
matrix = [[0, 1, 2, -1], [3, 4, 5, -2], [6, 7, 8, -3]]
while True:
    p1 = float(input('Type smaller number p1: '))
    p2 = float(input('Type higher number p2: '))
    if p1 <= p2:
        break
    else:
        print('p1 must be smaller than p2! Type again.')
counter = 0
for i in matrix:
    for j in i:
        if p1 <= j <= p2:
            counter += 1
print(counter)