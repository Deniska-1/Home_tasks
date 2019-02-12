# Задача 1
def sieve(until_number):
    if until_number < 2:
        return [0]
    if until_number == 2:
        return [2]
    else:
        list_of_numbers = [2] + [ x for x in range(3, until_number + 1, 2)]
    number_for_crossing, step, counter = 9, 3, 1
    while True:
        if step ** 2 > until_number:
            return list_of_numbers
        if number_for_crossing > until_number:
            counter += 1
            number_for_crossing, step, = list_of_numbers[counter] ** 2, list_of_numbers[counter]
        if number_for_crossing in list_of_numbers:
            list_of_numbers.remove(number_for_crossing)
        number_for_crossing += (2 * step)


print(sieve(100))


def test_func():
    if sieve(-2) == [0] and sieve(15) == [2, 3, 5, 7, 11, 13]:
        print('All right!')
    else:
        print('You have a mistake in your function!')


test_func()