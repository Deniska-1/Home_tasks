import json


def my_dec(func):
    def my_function():
        result = func()
        try:
            line = json.dumps(result)
            with open('json', 'a') as file:
                file.write(line)
        except:
            with open('text', 'a') as file:
                file.write(result + '\n')
        return lambda : ...
    return my_function



@my_dec
def my_func():
    print('word')
    smth_new = {'key' : 'dfsg'}
    return smth_new


my_func()