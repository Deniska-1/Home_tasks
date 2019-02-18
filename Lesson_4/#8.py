# Задача 8
grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6) ]
new_grades = []
for i in grades:
    new_grades.append([i[1], i[0]])
new_grades.sort(reverse=False)
for i in new_grades:
    print('Hello', i[1] + '!', 'Your grade is', i[0])