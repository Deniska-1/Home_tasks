# Задача 0
first_list = [1, 3, 4, 56, 0, 34, 0, 23, 0]
first_dict = {}
for i in first_list:
    if not first_dict.get(i, 0):
        first_dict[i] = 1
    else:
        first_dict[i] += 1
numbers, counter = [], 0
for i, j in first_dict.items():
    if j > counter:
        counter = j
        numbers = []
        numbers.append(i)
    elif j == counter:
        numbers.append(i)

print('Item(s)', numbers, 'is(are) in list', counter, 'time(s).')