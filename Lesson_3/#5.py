string_1 = input('Type the first string: ')
string_2 = input('Type the second string: ')
if string_2.find(string_1) != -1:
    print('the second string is a part of the first string')
else:
    print('the second string is not a part of the first string')
