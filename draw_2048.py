def draw_matrix_lines():
    global new_value_Y, new_value_X
    char_long = 5
    for hi in range(h):
        matrix_line = ''
        matrix_empty_line = ''
        for wi in range(w):
            spaces = ' ' * (char_long + 1 - len(str(Matrix[hi][wi])))
            spaces_end = ' ' * char_long
            if Matrix[hi][wi] == 0:
                matrix_line += int_to_color(hi, wi) + spaces_end + '-' + spaces_end
            else:
                matrix_line += int_to_color(hi, wi) + spaces + str(Matrix[hi][wi]) + spaces_end
            matrix_empty_line += int_to_color(hi, wi) + spaces_end + ' ' + spaces_end + '\x1b[0m'
        print(matrix_empty_line)
        print(matrix_line + '\x1b[0m')
        print(matrix_empty_line)


def draw_matrix():
    os.system('clear')
    print('2048 GAME // Score: ' + str(points) + '\n')
    if (empty_mapping() > 0):
        draw_matrix_lines()
    else:
        if (isMerged() == False):
            draw_matrix_lines()
            print('')
            spaces = ' ' * 20
            print('\x1b[1;33;40m' + spaces * 2)
            print(' ' * 15 + 'GAME OVER!' + ' ' * 15)
            print(spaces * 2 + '\n\x1b[0m')
        else:
            draw_matrix_lines()


def int_to_color(iy, ix):
    global new_value_X, new_value_Y
    icolor = Matrix[iy][ix]
    ret_color = '\x1b[0;30;47m'
    if icolor == 0:
        ret_color = '\x1b[1;30;47m'
    if icolor == 2:
        ret_color = '\x1b[1;36;40m'
    if icolor == 4:
        ret_color = '\x1b[1;35;40m'
    if icolor == 8:
        ret_color = '\x1b[1;34;40m'
    if icolor == 16:
        ret_color = '\x1b[1;33;40m'
    if icolor == 32:
        ret_color = '\x1b[1;32;40m'
    if icolor == 64:
        ret_color = '\x1b[1;31;40m'
    if icolor == 128:
        ret_color = '\x1b[1;31;40m'
    if icolor == 256:
        ret_color = '\x1b[1;31;40m'
    if icolor == 512:
        ret_color = '\x1b[1;31;40m'
    if icolor == 1024:
        ret_color = '\x1b[1;31;40m'
    if icolor == 2048:
        ret_color = '\x1b[1;31;40m'
    if icolor == 4096:
        ret_color = '\x1b[1;31;40m'
    if icolor == 8192:
        ret_color = '\x1b[1;31;40m'

    if iy == new_value_Y and ix == new_value_X:
        ret_color = '\x1b[0;30;43m'

    return ret_color
