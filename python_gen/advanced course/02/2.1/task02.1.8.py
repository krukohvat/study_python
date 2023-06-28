n = int(input())
k = int(input())
sp = [i for i in range(1, n+1)]
flag = True
for i in range(1, len(sp)+1):
    if i%k != 0:
        sp.append(i)
    else:
        pass
print(sp[len(sp)-1])