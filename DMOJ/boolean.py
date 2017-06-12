string = input()

if string[-4:] == 'True':
    if ((len(string)-4)/4) %2== 0:
        print('True')
    else:
        print('False')
else:
    if ((len(string)-5)/4) %2== 1:
        print('True')
    else:
        print('False')