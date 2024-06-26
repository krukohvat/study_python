'''
Напишите программу, которая выводит максимальный элемент в области ниже главной диагонали матрицы.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
''' 
n = int(input())
sp = []
for j in range(n):
    ls_j = input().split()
    sp += [[int(ls_j[i]) for i in range(len(ls_j))]]
max = sp[0][0]
for i in range(1, n):
    for j in range(0, i+1):
        if sp[i][j] > max:
            max = sp[i][j]
print(max)