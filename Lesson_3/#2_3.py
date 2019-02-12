string = 'Hello!Anthony!Have!A!Good!Day!'
results_list = []
for i in string.upper().split('!'):
    if i:
        results_list.append(i)
print(results_list)
sort_list = results_list[:]
sort_list.sort()
for i in sort_list:
    print(i)