# объявление функции
def number_to_words(num):
    dozens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    from_10_to_19 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    numbers = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    if n < 10:
        return numbers[n]
    elif 10 <= n < 20:
        return from_10_to_19[n-10]
    else:
        return dozens[n//10]+' '+numbers[n%10]
    
    
# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))