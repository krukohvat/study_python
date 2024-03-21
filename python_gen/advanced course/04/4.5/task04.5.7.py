'''
Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
'''
n = int(input())
mx = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    for j in range(n-1, -1, -1):
        print(mx[j][i], end=' ')
    print()