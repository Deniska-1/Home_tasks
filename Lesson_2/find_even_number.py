first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
if first_number * second_number * third_number % 2 == 0:
    print(max(first_number, second_number, third_number))
else:
    print(min(first_number, second_number, third_number))