'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
n = int(input())
in_lst = [[j for j in input().split()] for k in range(n)]
max_val = in_lst[0][n-1]
for i in range(n):
    for j in range(n):
        if (in_lst[i][j] > max_val) and (j>=n-1-i):
            max_val = in_lst[i][j]
print(max_val)