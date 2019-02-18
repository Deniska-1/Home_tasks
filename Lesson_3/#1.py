list = ['a', 'b', 'c', 'd', 'n'] # simple list, for example
max_number = max(list)

if len(list) == list.index(max(list)) + 1:
    new_list = list[:len(list)-1]
else:
    new_list = list[:list.index(max(list))] + list[list.index(max(list))+1:]

print(new_list)
