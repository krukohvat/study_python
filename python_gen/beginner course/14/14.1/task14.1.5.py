# объявление функции
def get_month(language, number):
    ru_month = ["0", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    en_month = ['0', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if lan == 'ru':
        return ru_month[num]
    else:
        return en_month[num]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))