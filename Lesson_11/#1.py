class Person():
    _number = 1

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self._number = self._number
        Person._number += 1


def search(dct, number=None, first_name=None, last_name=None, gender=None, age=None):
    phantom_dict = {}
    virtual_dict = {'number': number, 'first_name': first_name, 'last_name': last_name, 'gender': gender, 'age': age}
    for i, j in virtual_dict.items():
        if j:
            if j == dct[i]:
                phantom_dict = dct
            elif j == '-':
                continue
            else:
                phantom_dict = {}
                break
    if phantom_dict:
        return phantom_dict


def print_result(**kwargs):
    for i, j in kwargs.items():
        print(i + ' : '+ j)


def open_database_txt(**kwargs):
    with open('DB.txt') as f:
        dct = {}
        while True:
            line = f.readline()
            if line:
                number, first_name, last_name, gender, age = line.split()
                dct = {'number': number, 'first_name': first_name, 'last_name': last_name,
                       'gender': gender, 'age': age}
                result_of_searching = search(dct, **kwargs)
                if result_of_searching:
                    print_result(**result_of_searching)
            else:
                break


def open_database_json(**kwargs):
    with open('DB_json.txt') as file_json:
        while True:
            line = file_json.readline().strip('\n').strip(',')
            if line == '][' or line == ']' or line == '[': continue
            if not line: break
            number, first_name, last_name, gender, age = json.loads(json.loads(line))
            dct = {'number': str(number), 'first_name': first_name, 'last_name': last_name,
                   'gender': gender, 'age': age}
            searching_result = search(dct, **kwargs)
            if searching_result:
                print_result(**searching_result)


def request_maker():
    full_request = {}
    while True:
        my_request = input('Type your request (name of column:value) or press Enter for finish\n'
                        '(Possible options of columns names: number, first_name, last_name, gender, age).\n'
                        'Use every column name only ones for one cycle of request: ').split(":")
        if my_request != ['']:
            full_request[my_request[0]] = my_request[1]
        else:
            return full_request


def add(action):
    while True:
        info = input('Enter information about person in format(first_name, last_name, gender, age)\n'
                     'or press Enter for finish. If you don\'t know some information about person\n'
                     'type - (For example: first_name, -, gender, -): ').split(', ')
        if info != ['']:
            person = Person(*info)
            if action == 'txt':
                writer_txt(person)
            else:
                writer_json(person)
        else:
            break


def writer_txt(person):
    with open('DB.txt', 'a') as file:
        person_data = ''
        for i in (person._number, person.first_name, person.last_name, person.gender, person.age):
            person_data += str(i) + ' '
        file.write(person_data)
        file.write('\n')


def writer_json(person):
    with open('DB_json.txt', 'a') as file_json:
        person_data = [json.dumps([str(person._number), person.first_name, person.last_name, person.gender, person.age])]
        file_json.write(json.dumps(person_data, indent=0))


while True:
    choice = input('Enter type of DataBase(Possible options: txt or json) or press Enter for finish: ')
    if choice == 'txt':
        action = input('Do you wanna find someone or add person in DataBase(Possible options: find or add): ')
        if action == 'find':
            request = request_maker()
            if request:
                open_database_txt(**request)
        elif action == 'add':
            add('txt')
    elif choice == 'json':
        import json

        action = input('Do you wanna find someone or add person in DataBase(Possible options: find or add): ')
        if action == 'find':
            request = request_maker()
            if request:
                open_database_json(**request)
        elif action == 'add':
            add('json')
    elif choice == '':
        break
    else:
        print('Unexpected answer! Check your input.')




