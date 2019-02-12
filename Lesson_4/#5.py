# Задача 5
first_list = [1, 3, 4, 56, 0, 34, 0, 23, 0]
counter = 0
for i in first_list:
    if not i:
        first_list.remove(0)
        counter += 1
first_list.extend([-1]*counter)
print(first_list)