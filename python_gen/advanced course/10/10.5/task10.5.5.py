'''В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.

Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).

Примечание 2. Выводить содержимое словаря result не нужно.'''
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(s.split()[i].split(':')[0]): s.split()[i].split(':')[1] for i in range(len(s.split()))}

#result = {int(k):v for k, v in [l.split(':') for l in s.split()]}