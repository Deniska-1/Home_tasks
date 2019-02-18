# Задача 0
list_of_numbers = []
while True:
    number = input('Type number or press "Enter" if you finished: ')
    if number:
        list_of_numbers.append(number)
    else:
        break
search_number = input('Enter the number to search: ')
print('Your number is on the list', list_of_numbers.count(search_number), 'time(s).')