appeal = input('Type the appeal (for example: Dear Mr. Smith): ')
if appeal.split()[1] == 'Mr.':
    print('Man')
elif appeal.split()[1] == 'Mrs.' or 'Miss' or 'Ms.':
    print('Woman')
else:
    print('Wrong appeal')