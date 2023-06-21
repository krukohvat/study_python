from math import *
# объявление функции
def get_circle(radius):
    length = 2*pi*r
    square = pi*(r**2)
    return length, square
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)