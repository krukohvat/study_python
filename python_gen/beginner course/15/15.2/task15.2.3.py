from random import *
print('Добро пожаловать в числовую угадайку')
while True:
    n = int(input(('Введите верхнюю границу: ')))
    num = randint(1, n)
    def is_valid(ch):
        return ch.isdigit() and 0<=int(ch)<=n
    k = 0
    a = 1
    while a == 1:
        print('Введите число от 1 до', n, ':', end=' ')
        ch = input()
        k += 1
        if is_valid(ch):
            ch = int(ch)
            if ch > num:
                print('Слишком много, попробуйте еще раз')
            elif ch < num:
                print('Слишком мало, попробуйте еще раз')
            else:
                a = 2
        else:
            print('А может быть все-таки введем целое число от 1 до', n, '?')
            continue
    if k%10 == 3 and k != 13:
        print('Вы угадали с ', k, '-ьей попытки, поздравляем!', sep='')
    else:
        print('Вы угадали с ', k, '-ой попытки, поздравляем!', sep='')
    answ = input('Хотите сыграть еще? Y(yes) / N(no): ').upper()
    if answ == "Y" or answ == "YES":
        a = 1
    else:
        break