def search(number=None, first_name=None, last_name=None, gender=None, age=None):
    if number:
        collection = {number : dct[number]}
    else:
        collection = {}
        for i in dct:
            phantom_dict = {}
            for j in [first_name, last_name, gender, age]:
                if j:
                    if j in dct[i].values():
                        phantom_dict = dct[i]
                    else:
                        phantom_dict = {}
                        break
            if phantom_dict:
                collection.update({i:phantom_dict})
    return print_result(**collection)


def print_result(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


# Functions from Lesson_5 #3
with open('DB.txt') as file:
    dct = {}
    while True:
        line = file.readline()
        if line:
            number, first_name, last_name, gender, age = line.split()
            dct[number] = {'first_name' : first_name, 'last_name' : last_name,
                           'gender' : gender, 'age' : age}
        else:
            break
    while True:
        full_request = {}
        while True:
            request = input('Type your request (name of column : value) or press Enter for finish: ').split(":")
            if request != ['']:
                full_request[request[0]] = request[1]
            else:
                break
        if full_request:
           search(**full_request)
        else:
            break