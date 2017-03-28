'''
- Feldarabolás: Main / mozgatás & reset / highscore / kirajzolás / menü
- Bugfix: Ha változás történik a mátrixban csak akkor adhat hozzá új értéket
- globális változók csökkentése
- High score fileba / Dedicated to Mark
- ha marad időnk: HP game (időre high score)
- docstrings
'''
##############################################################################

# 2048 another program menus
from menu_2048 import *
from move_2048 import *
from highscore_2048 import *


# MAIN THREAD
choose_menu()

add_rand_number()
add_rand_number()
draw_matrix()

while True:
    print('')
    c = input('MOVE: w/a/s/d | EXIT: x | NEW GAME: n | YOUR CHOICE? ')
    if c == ('w'):
        up()
    if c == ('s'):
        down()
    if c == ('a'):
        left()
    if c == ('d'):
        right()
    if c == ('x'):
        break
    if c == ('n'):
        reset_matrix()
        choose_menu()
        add_rand_number()
        add_rand_number()
        draw_matrix()
    else:
        draw_matrix()
