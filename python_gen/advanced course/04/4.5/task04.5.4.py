'''
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.'''
n = int(input())
mx = [[int(j) for j in input().split()] for i in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if mx[i][j] == mx[j][i]:
            continue
        else: 
            flag = False
if flag == True:
    print('YES')
else:
    print("NO")