'''
you input a value. a program return to you a square matrix
'''
n = int(input())
def print_mx(n):
    sp =[]
    while True:
        if (n**0.5) - int((n**0.5)) != 0:
            n -= 1
        else:
            break
    x = int(n**0.5)
    for j in range(int(n**0.5)):
        ls = [i+1 for i in range(x-int(n**0.5), x)]
        sp += [ls]
        ls = []
        x += int(n**0.5)
    for i in range(len(sp)):
        for j in range(len(sp[i])):
            print(str(sp[i][j]).ljust(6), end='')
        print()
print_mx(n)