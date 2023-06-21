# объявление функции
def is_prime(num):
    flag = True
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))