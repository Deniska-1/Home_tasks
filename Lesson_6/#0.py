# Задача 0
def len_of_words(new_string=None, separator=None):
    if not new_string:
        new_string = input('Type your text: ')
    if not separator:
        separator = input('Type separator: ')
        # Условия введены, что бы проще было использовать проверяющую функцию (этакий кастыль).
    list_of_words = new_string.split(separator)
    for i, j in enumerate(list_of_words):
        list_of_words[i] = str(len(j)) + j
    return list_of_words


print(len_of_words())


def test_func():
    if len_of_words('asd d ddd fef', ' ') == ['3asd', '1d', '3ddd', '3fef']:
        print('All right!')
    else:
        print('You have a mistake in your function!')


test_func()