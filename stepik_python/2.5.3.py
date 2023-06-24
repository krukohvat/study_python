a = [int(i) for i in input().split()]
a.sort()
s = []
for i in a:
    if (i not in s) and (a.count(i)>1):
        s += [i]
print(*s)