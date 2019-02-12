with open('Data_file.txt', 'a') as file:
    while True:
        line = input('Type new line or press Enter for finish: ')
        if line:
            file.write(line + '\n')
        else:
            break
