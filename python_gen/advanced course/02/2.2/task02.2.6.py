n = int(input())
sp = [int(input()) for i in range(n)]
ch = int(input())
flag = False
for i in range(len(sp)):
    for j in range(i, len(sp)):
        if i != j:
            if sp[i]*sp[j] == ch:
                flag = True
                break
if flag == True:
    print('ДА')
else:
    print('НЕТ')