# Задача 1
word = input('Type your word: ')
if ord(word[0]) == 95 or 64 < ord(word[0]) < 91 or 96 < ord(word[0]) < 123:
    print('Your word', word, 'can be identifier.')
else:
    print('Your word', word, 'can not be identifier.')