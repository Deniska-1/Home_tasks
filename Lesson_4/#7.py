# Задача 7
first_string = input('Type your string: ')
new_symbol = input('Type your symbol: ')
new_string = ''
counter = 0
while True:
    if first_string.find(new_symbol, counter) == -1:
        new_string = new_string[:len(new_string)-1]
        break
    else:
        new_string += first_string[counter:first_string.find(new_symbol, counter)]
        print(first_string[counter:first_string.find(new_symbol, counter)])
        new_string += new_symbol.upper()
        counter = first_string.find(new_symbol, counter) + 1
print(new_string)