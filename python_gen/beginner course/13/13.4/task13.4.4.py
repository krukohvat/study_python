# объявление функции
def get_factors(num):
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
            result = len(l)
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))