a = [int(i) for i in input().split()]
a.sort()
s = []
for i in a:
    print('a_do=', a, ' i=', i, end=' ')
    if a.count(i) > 1:
        s += [i]
        while i in a:
            a.remove(i)
            #print('a', a, end='')
    print('s=', s)
    print('a_posle=', a)
print(*s)