'''
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
'''
n = int(input())
mx = [[int(j) for j in input().split()][::-1] for i in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if mx[i][j] == mx[j][i]:
            continue
        else: 
            flag = False
            break
if flag == True:
    print('YES')
else:
    print("NO")