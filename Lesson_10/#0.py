import time


"""def dec0(func):
    time1 = time.time()
    
    def in_func():
        func(1000)
        time2 = time.time()
        return lambda: float(time2) - float(time1)
    
    return in_func()


def dec1(func):
    time1 = time.time()

    def in_func(arg):
        func(arg)
        with open('Data.txt', 'a') as file:
            time2 = time.time()
            file.write(str(float(time2) - float(time1)) + '\n')
            file.write(func.__name__ + '\n')
            file.write(str(arg) + '\n')
        return lambda self: self

    return in_func

# Print type(arg)
def dec2(func):

    def in_func(*arg):
        for i in arg:
            print(type(i))
        return lambda self: self

    return in_func



def dec3(func):

    def in_func(arg, dct = {}):
        print(in_func.__defaults__[0])
        if arg not in in_func.__defaults__[0]:
            dct[arg] = func(arg)
            return dct[arg]
        else:
            result = in_func.__defaults__[0][arg]
            print(result)
            return result

    return in_func
"""

#@dec3
#@dec2
#@dec1
#@dec0
def sieve(until_number):
    if until_number < 2:
        return [0]
    if until_number == 2:
        return [2]
    else:
        list_of_numbers = [2] + [x for x in range(3, until_number + 1, 2)]
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


print(sieve(10))
print(sieve(20))
print(sieve(10))