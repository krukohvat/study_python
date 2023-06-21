sp = [int(i) for i in input().split()]
for i in range(-len(sp), -1, 2):
    sp[i], sp[i+1] = sp[i+1], sp[i]
print(*sp)