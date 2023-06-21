# объявление функции
def merge():
    result = []
    n = int(input())
    for i in range(n):
        numbers = []
        numbers = [int(c) for c in input().split()]
        numbers.sort()
        result.extend(numbers)
        result.sort()
    print(*result, end=' ')

# вызываем функцию
merge()