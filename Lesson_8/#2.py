with open('Test_results.txt') as file:
    counter = 0
    marks_sum = 0
    while True:
        line = file.readline()
        if line:
            mark = int(line.split()[-1])
            marks_sum += mark
            counter += 1
            if mark < 3:
                print(line, end = '')
        else:
            break
    print(marks_sum / counter)