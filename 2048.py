'''
- Feldarabolás: Main / mozgatás & reset / highscore / kirajzolás / menü
- Bugfix: Ha változás történik a mátrixban csak akkor adhat hozzá új értéket
- globális változók csökkentése
- High score fileba / Dedicated to Mark
- ha marad időnk: HP game (időre high score)
'''
##############################################################################
from random import randint
import os
import curses
import time

# 2048 another program menus
import draw_2048
import menu_2048
import move_2048
import highscore_2048.py

numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
empty_X = []
empty_Y = []
points = 0
w = 6
h = 5
Matrix = [[0 for x in range(w)] for y in range(h)]
temp_array = []
new_value_X = -1
new_value_Y = -1
act_move = 0
last_move = -1


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
