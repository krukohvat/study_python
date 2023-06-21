s = input()
qwe = ''
for i in s:
    k = str(s.count(i))
    #s = s.replace(i, i+k)
    if i not in qwe:
        qwe += i+k
    #print(i, k, sep='', end='')
print(qwe)