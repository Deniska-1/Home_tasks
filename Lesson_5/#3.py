# Задача 3
'''Первая функция добавляет студента в словарь.
Вторая ищет студентов по ключу (номеру) или по одному или нескольким признакам. 
В последнем случае, создается словарь, куда закидываются все студенты, все сразу совпавшие признаки.
Последняя функция выводит полученные значения построчно: Номер словарь_информации'''
def add_student(number, first_name, last_name, gender, age):
    dict_of_students[number] = {'first name' : first_name,
                                'last name' : last_name,
                                'gender' : gender,
                                'age' : age}


def search(number=None, first_name=None, last_name=None, gender=None, age=None):
    if number:
        collection = {number : dict_of_students[number]}
    else:
        collection = {}
        for i in dict_of_students:
            phantom_dict = {}
            for j in [first_name, last_name, gender, age]:
                if j:
                    if j in dict_of_students[i].values():
                        phantom_dict = dict_of_students[i]
                    else:
                        phantom_dict = {}
                        break
            if phantom_dict:
                collection.update({i:phantom_dict})
    return print_result(**collection)


def print_result(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


dict_of_students = {}
add_student('1', 'Vasya', 'Lech', 'Male', 32)
add_student('2', 'Vera', 'Miko', 'Female', 22)
add_student('3', 'Ira', 'Hinuchko', 'Female', 43)
add_student('4', 'Misha', 'Durov', 'Male', 18)
search('3')
search(None, 'Vera', None, 'Female', None)
search(None, None, None, 'Male', None)
