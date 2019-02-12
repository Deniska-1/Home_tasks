# Задача 4
matrix = [[0, 1, 2, -3], [3, 4, 5, 100], [6, 7, 8, -23], [98, 0, 33, 1]]
matrix_len = len(matrix)
sum_of_positive_items = 0
for i in range(matrix_len):
    for j in range(i, matrix_len):
        item = matrix[i][j]
        if item > 0:
            sum_of_positive_items += item
print(sum_of_positive_items)