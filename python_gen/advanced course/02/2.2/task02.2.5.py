a = [int(i) for i in input().split()]
s = []
for i in a:
    if i not in s:
        s += [i]
print(len(s))