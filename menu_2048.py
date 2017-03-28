def custom_size():
    global h, w
    os.system('clear')
    print('2048 GAME\n')
    w_inp = input('Set width: ')
    try:
        w = int(w_inp)
    except ValueError:
        print ('You got the default value: ' + str(w) + '\n')

    h_inp = input('Set height: ')
    try:
        h = int(h_inp)
    except ValueError:
        print ('You got the default value: ' + str(h) + '\n')
        input('\nPRESS ANY KEY TO CONTINUE')
    gen_matrix()


def choose_menu():
    global h, w
    os.system('clear')
    print('2048 GAME\n')
    print('(e)asy       6x6')
    print('(n)ormal     5x5')
    print('(h)ard       4x4')
    print('(i)mpossible 3x3\n')
    print('(c)ustom size\n')
    diff_in = input('Choose difficulty: ')
    if diff_in == 'e':
        h = 6
        w = 6
        gen_matrix()

    if diff_in == 'n':
        h = 5
        w = 5
        gen_matrix()

    if diff_in == 'h':
        h = 4
        w = 4
        gen_matrix()

    if diff_in == 'i':
        h = 3
        w = 3
        gen_matrix()

    if diff_in == 'c':
        custom_size()
