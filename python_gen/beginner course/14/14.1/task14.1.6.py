# объявление функции
def is_magic(date):
    ls = [int(i) for i in date.split('.')]
    return ls[0]*ls[1] == ls[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))