from math import *
# объявление функции
def compute_binom(n, k):
    a = factorial(n-k)
    return int(factorial(n)/(factorial(k) * a))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))