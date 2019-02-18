# Задача 2
phrase = input('Type your text: ')
list_of_words = phrase.lower().split()
list_of_words.sort(key=len, reverse=False)
print(set(list_of_words[0]).intersection(set('aeiou')))