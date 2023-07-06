'''Тимур и его числа
Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше") Руслан может гарантированно угадать число Тимура?
'''
from math import *
from random import *
ch = int(input())
num = randint(1, ch)
if round(log(ch, 2)) >= log(ch, 2):
    print(round(log(ch, 2)))
else:
    print(round(log(ch, 2))+1)