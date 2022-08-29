def func1(a):
    if str(a)[0:-1] == str(a)[-1:0:-1]:
        print('является')
    else:
        print('не является')

func1('шалаш')
