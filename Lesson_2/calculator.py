first_operator = input('Enter first operator: ')
second_operator = input('Enter second operator: ')
operator = input('Enter operator: ')
if operator not in ['+', '-', '/', '*']:
    print('Result: NaN')
else:
    if operator == '+':
        result = float(first_operator) + float(second_operator)
    elif operator == '-':
        result = float(first_operator) - float(second_operator)
    elif operator == '*':
        result = float(first_operator) * float(second_operator)
    elif operator == '/':
        if second_operator != 0:
            result = float(first_operator) / float(second_operator)
        else:
            result = 'Inposible operation'
    print('Resalt:', result)
