import json


"""
# How create json-file
with open('DB.txt') as file, open("DB_json.txt", 'a') as file_json:
    lst = []
    while True:
        line = file.readline()
        if line != '':
            number, first_name, last_name, gender, age = line.strip().split()
            lst.append(json.dumps([number, {'first_name' : first_name, 'last_name' : last_name, 'gender' : gender, 'age' : age}]))
        else:
            break
    file_json.write(json.dumps(lst, indent=0))
"""


def search(number=None, first_name=None, last_name=None, gender=None, age=None):
    collection = {}
    with open('DB_json.txt') as file_json:
        while True:
            line = file_json.readline().strip('\n').strip(',')
            if line == '[' or line == ']': continue
            if not line: break
            line = json.loads(json.loads(line))
            phantom_dict = {}
            if line[0] == number:
                phantom_dict[number] = line[1]
            for j in [first_name, last_name, gender, age]:
                if j:
                    if j in line[1].values():
                        if not number:
                            phantom_dict[line[0]] = line[1]
                    else:
                        phantom_dict = {}
                        break
            if phantom_dict:
                collection.update(phantom_dict)
        return print_result(**collection)


def print_result(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


while True:
    full_request = {}
    while True:
        request = input('Type your request (name of column:value) or press Enter for finish: ').split(":")
        if request != ['']:
            full_request[request[0]] = request[1]
        else:
            break
    if full_request:
        search(**full_request)
    else:
        break