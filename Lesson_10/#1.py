import os
'''Все обходит, без циклов. Едиственная проблема, папки и файлы вперемешку. Не знаю, как отсортировать.'''


def catalog(path, pr_path=[], counter=0, obj=[], rest_files=[], key=False):
    files = rest_files or os.listdir(path)
    if not (pr_path == obj == rest_files == [] and counter == 0 and key):
        key = True
        try:
            os.listdir(path+'/'+files[0])
            print('|' + '_' * counter * 2 + files[0])
            pr_path.append(files[0])
            obj.append(files[1:])
            catalog(path+'/'+files[0], pr_path, counter + 1, obj, key=key)
        except:
            print('|' + '_' * counter * 2 + files[0])
            if not len(files) == 1:
                catalog(path, pr_path, counter, obj, files[1:], key=key)
            else:
                catalog(path[:len(path)-len(pr_path[-1])-1], pr_path[:-1], counter - 1, obj[:-1], rest_files=obj[-1], key=key)


catalog(input('Enter directory path: '))