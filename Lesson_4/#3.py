# Задача 3
list_of_strings = []
counter = 0
while True:
    new_string = input('Type string or press "Enter" if you finished: ')
    if new_string:
        list_of_strings.append((counter, len(new_string), new_string))
        counter += 1
    else:
        break
len_string = 0
our_collection = []
for i in range(len(list_of_strings)):
    if list_of_strings[i][1] > len_string:
        our_collection = []
        our_collection.append(list_of_strings[i][0])
        len_string = list_of_strings[i][1]
    elif list_of_strings[i][1] == len_string:
        our_collection.append(list_of_strings[i][0])
print('Number(s) the longest string(s) is(are):', our_collection)
