'''Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
n = int(input())
mx = [[int(j) for j in input().split()] for i in range(n)]
m = int(input())
mx_copy = [i[:] for i in mx]
val = 0
mx_mid = [[0]*n for i in range(n)]
while m > 1:
    for i in range(n):
        for j in range(n):
            for r in range(n):
                val += mx_copy[i][r]*mx[r][j]
            mx_mid[i][j] = val
            val = 0
    mx = [i[:] for i in mx_mid]
    m -= 1
for i in range(n):
    for j in range(n):
        print(mx[i][j], end=' ')
    print()