'''
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.
'''
n = int(input())
sum = 0
sp = []
for j in range(n):
    ls_j = input().split()
    sp += [[int(ls_j[i]) for i in range(len(ls_j))]]

for i in range(n):
    sum += sp[i][i]
print(sum)