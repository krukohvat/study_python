# объявление функции
def get_factors(num):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))