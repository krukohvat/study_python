# объявление функции
def get_days(month):
    if str(num) in '13578' or num == 10 or num == 12:
        result = 31
    elif str(num) in '469' or num == 11:
        result = 30
    else:
        result = 28
    return result

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))