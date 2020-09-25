def calculator():
    ope = input('''which operation you wish to do + para ad - para sub * para mult / para div''')
    
    n_1 = int(input('n1'))
    n_2 = int(input('n2'))
    
    if ope == '+':
        print('{} + {} = '.format(n_1,n_2))
        print(n_1 + n_2)
        
    elif ope == '-':
        print('{} + {} = '.format(n_1,n_2))
        print(n_1 + n_2)

    elif ope == '*':
        print('{} + {} = '.format(n_1,n_2))
        print(n_1 + n_2)

    elif ope == '/':
        print('{} + {} = '.format(n_1,n_2))
        print(n_1 + n_2)
    
    else:
        print('okay')

        return

calculator()