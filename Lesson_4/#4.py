# Задача 4
import math
first_sum, second_sum = 1000, 1100
percent = float(input('Type your percent (0 < percent < 25): ' ))
time = math.ceil(math.log(second_sum/first_sum, 10)/math.log(1 + percent / 100, 10))
print(time, 'Month(s),', round(first_sum*(1 + percent / 100) ** time, 4), 'BYN')

# Или так
first_sum, second_sum = 1000, 1100
percent = float(input('Type your percent (0 < percent < 25): ' ))
time = 0
while first_sum < second_sum:
    first_sum *= (1 + percent / 100)
    time += 1
print(time, 'Month(s),', round(first_sum, 4), 'BYN')