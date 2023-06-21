# объявление функции
def get_shipping_cost(quantity):
    if n == 1:
        return "1000"
    else:
        a = 1000 + 120*(n-1)
        return a

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))