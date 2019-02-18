# Задача 1.
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
average = 0
for i in matrix:
    average += sum(i)
print(average / len(matrix)**2)