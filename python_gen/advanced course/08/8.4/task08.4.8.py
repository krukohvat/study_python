'''Одинаковые наборы
На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?

Формат входных данных
На вход подаются две строки, состоящие из цифр.

Формат выходных данных
Программа должна вывести YES, если для записи этих строк были использованы одинаковые наборы цифр и NO, в противном случае.'''
if sorted(set(input())) == sorted(set(input())):
    print("YES")
else:
    print("NO")
