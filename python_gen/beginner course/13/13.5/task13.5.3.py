# объявление функции
def get_next_prime(num):
    k = n+1
    flag = True
    while flag == True:
        for i in range(2, k//2 +1):
            if k % i == 0:
                flag = True
                break
        else:
            flag = False
        k += 1
    return k-1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))