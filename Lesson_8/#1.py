with open('Data_file.txt') as file:
    counter = 0
    list_of_info = []
    while True:
        line = file.readline()
        if line:
            list_of_info.append({'lines_number' : counter, 'letters' : len(line),
                                 'words' : len(line.split())})
            counter += 1
        else:
            break
    print(counter, list_of_info)