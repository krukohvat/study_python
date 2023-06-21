spisok = [int(i) for i in input().split()]
a = 0
for i in range(1, len(spisok)):
    if spisok[-i] > spisok[-i-1]:
        a += 1
print(a)